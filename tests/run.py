from testing import test

def main():
    reports_name: list[str] = ['report_LLAMA', 'report_OPENAI', 'report_HyDE', 'report_GEMINI']

    while True:
        print()
        for index, report in enumerate(reports_name):
            print(f'{index+1}: {report}')
            
        try:
            choice = int(input("\nSelect the report number you want to run. By selecting 0 end the program. \nChoice:"))
            if choice == 0:
                break

            result = reports_name[choice-1]
            print(f'\n{result}\n')
            test(result).run()
            break

        except IndexError:
            print(f'There is no such number with the report\n')

        except ValueError:
            print(f'Enter the number\n')

if __name__ == '__main__':
    main()