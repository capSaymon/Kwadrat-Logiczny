import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import glob
import os

class results():
    def __init__(self, file_name, prompt_technique=2):
        self.file_name = file_name
        self.prompt_technique = prompt_technique 

        if self.prompt_technique == 0:
            self.file_name = self.file_name+'_zero_shot'
        elif self.prompt_technique == 1:
            self.file_name = self.file_name+'_one_shot'
        elif self.prompt_technique == 3:
            self.file_name = self.file_name+'_self_consistency'
        elif self.prompt_technique == 4:
            self.file_name = self.file_name+'_chain_of_thought'

    def run(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        QUESTIONS_PATH = os.path.join(BASE_DIR, 'reports')

        if not os.path.exists(QUESTIONS_PATH):
            raise FileNotFoundError("folder not found")
        
        file_path = glob.glob(os.path.join(QUESTIONS_PATH, f'{self.file_name}.csv'))
        if not file_path:
            raise FileNotFoundError("file not found")

        df = pd.read_csv(file_path[0])
        metrics = ['Attempts', 'Format Success', 'Relation Success', 'First Aproach Successful']
        grouped = df.groupby('Question')

        questions = []
        data = {metric: [] for metric in metrics}

        print('=' * 50)
        print(f"{self.file_name}\nValues for questions:\n")
        for question, group in grouped:
            print(f"{question}")
            questions.append(question)

            for metric in metrics:
                if metric == 'First Aproach Successful':
                    value = round(group[metric].mean())
                    print(f"  Mean {metric}: {value}")
                else:
                    value = group[metric].sum()
                    print(f"  Sum {metric}: {value}")
                data[metric].append(value)

            print('\n\n')
        print('=' * 50)


        x = np.arange(len(questions))
        width = 0.2

        fig, ax = plt.subplots(figsize=(12, 6))

        for i, metric in enumerate(metrics):
            offset = (i - 1.5) * width
            ax.bar(x + offset, data[metric], width, label=metric)

        ax.set_xlabel('Question')
        ax.set_ylabel('Value')
        ax.set_title(f'{self.file_name}')
        ax.set_xticks(x)
        ax.set_xticklabels(questions, rotation=45, ha='right')
        ax.legend()

        plt.tight_layout()
        plt.show()