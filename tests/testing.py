import os
import sys
import csv
import time
import statistics

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from LLAMA.ML_llama import llama
from OPENAI.ML_openai import gpt
from HyDE.RAG import rag
from GEMINI.ML_gemini import gemini
from check_sentences import SentenceChecker


class Test():
    def __init__(self, report_file_name, prompt_technique):
        self.report_file_name = report_file_name
        self.prompt_technique = prompt_technique 


    def run(self):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        QUESTIONS_PATH = os.path.join(BASE_DIR, 'questions')

        if not os.path.isdir(QUESTIONS_PATH):
            print(f'Folder "questions" does not exist: {QUESTIONS_PATH}')
            return None
        
        while True:
            try:
                number_of_tests = int(input("\nSelect the number of tests: "))
                if number_of_tests <= 0:
                    raise IndexError
                break

            except IndexError:
                print(f'Incorrect quantity\n')

            except ValueError:
                print(f'Enter the number\n')

        
        for file_name in os.listdir(QUESTIONS_PATH):
            if not file_name.endswith('.txt'):
                continue
            base_name = os.path.splitext(file_name)[0]
            print(f'\nFile: {base_name}')

            format_success: int = 0
            relation_success: int = 0
            first_aproach_successful: int = 0
            times = []
            
            for i in range(number_of_tests):
                if self.report_file_name == 'report_LLAMA':
                    question, outcome, end_time, start_time = self.run_LLAMA(base_name)
                elif self.report_file_name == 'report_OPENAI':
                    question, outcome, end_time, start_time = self.run_OPENAI(base_name)
                elif self.report_file_name == 'report_HyDE':
                    question, outcome, end_time, start_time = self.run_HyDE(base_name)
                elif self.report_file_name == 'report_GEMINI':
                    question, outcome, end_time, start_time = self.run_GEMINI(base_name)
                else:
                    print('there is no such llm report name')

                result_time = end_time - start_time
                times.append(result_time)

                check = SentenceChecker(question, outcome)

                try:
                    check.test_response_format()
                    format_success += 1
                    if check.test_relation_between_sentences():
                        relation_success += 1
                    
                        if not first_aproach_successful:
                            first_aproach_successful = i + 1
                        self.save(f'result_{base_name}', outcome, i+1, self.report_file_name[7:])
                except AssertionError:
                    pass
            
            average_time = statistics.mean(times)
            min_time = min(times)
            max_time = max(times)

            data: str = f"\n\nAttempts: {number_of_tests} \nFormat success: {format_success} \nRelation success: {relation_success} \nFirst aproach successful: {first_aproach_successful}\n\n"
            line: str ='='*50
            print(line,data,line)
            self.save_data_to_csv(self.report_file_name, file_name[:-4], number_of_tests, format_success, relation_success, first_aproach_successful, average_time, min_time, max_time)


    def save(self, file_name: str, data: str, index: str, LLM: str =''):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        QUESTIONS_PATH = os.path.join(BASE_DIR, 'result_test')
        
        if not os.path.exists(QUESTIONS_PATH):
            os.makedirs(QUESTIONS_PATH)

        file_path = os.path.join(QUESTIONS_PATH, f'{file_name}.txt')
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(f'{LLM}\nApproach {index}\n{data}\n\n')


    def save_data_to_csv(self, report_file_name, question, number_of_attempts, format_success, relation_success, first_aproach_successful, average_time, min_time, max_time):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        QUESTIONS_PATH = os.path.join(BASE_DIR, 'reports')

        if self.prompt_technique == 0:
            report_file_name = report_file_name+'_zero_shot'
        elif self.prompt_technique == 1:
            report_file_name = report_file_name+'_one_shot'
        elif self.prompt_technique == 3:
            report_file_name = report_file_name+'_self_consistency'
        elif self.prompt_technique == 4:
            report_file_name = report_file_name+'_chain_of_thought'
        elif self.prompt_technique == 5:
            report_file_name = report_file_name+'_ReAct'

        os.makedirs(QUESTIONS_PATH, exist_ok=True)
        file_path = os.path.join(QUESTIONS_PATH, f'{report_file_name}.csv')
        file_exists = os.path.isfile(file_path)

        with open(file_path, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            if not file_exists:
                writer.writerow(['Question', 'Attempts', 'Format Success', 'Relation Success', 'First Aproach Successful', 'Average Time', 'Min Time', 'Max Time'])

            writer.writerow([ question, number_of_attempts, format_success, relation_success, first_aproach_successful, f"{average_time:.3f}", f"{min_time:.3f}", f"{max_time:.3f}" ])



    def run_LLAMA(self, base_name: str):
        llama_instance = llama(file_name=base_name, prompt_technique=self.prompt_technique)
        start_time = time.time()
        question, outcome = llama_instance.run_test()
        end_time = time.time()
        return question, outcome, end_time, start_time


    def run_OPENAI(self, base_name: str):
        openai_instance = gpt(file_name=base_name, prompt_technique=self.prompt_technique)
        start_time = time.time()
        question, outcome = openai_instance.run_test()
        end_time = time.time()
        return question, outcome, end_time, start_time


    def run_HyDE(self, base_name: str):
        rag_instance = rag(file_name=base_name)
        start_time = time.time()
        question, outcome = rag_instance.run_test()
        end_time = time.time()
        return question, outcome, end_time, start_time


    def run_GEMINI(self, base_name: str):
        gemini_instance = gemini(file_name=base_name, prompt_technique=self.prompt_technique)
        start_time = time.time()
        question, outcome = gemini_instance.run_test()
        end_time = time.time()
        return question, outcome, end_time, start_time