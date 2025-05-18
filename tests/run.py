from testing import test
from graph import results

def main():
    reports_name: list[str] = ['report_LLAMA', 'report_OPENAI', 'report_HyDE', 'report_GEMINI']

    while True:
        print()
        for index, report in enumerate(reports_name):
            print(f'{index+1}: {report}')
            
        try:
            choice = int(input("\nSelect the report number you want. By selecting 0 end the program. \nChoice:"))
            if choice == 0:
                break

            name = reports_name[choice-1]
            print(f'\n{name}\n')

            choice = input("\nRun tests? (y/n)").strip().lower()[0]
            if choice == "y":
                test(name).run()
            elif choice == "n":
                pass
            else:
                raise ValueError

            choice = input("\nShow report of all tests? (y/n)").strip().lower()[0]
            if choice == "y":
                results(name).run()
            elif choice == "n":
                break
            else:
                raise ValueError

        except IndexError:
            print(f'There is no such number with the report\n')

        except ValueError:
            print(f'Wrong answer\n')

if __name__ == '__main__':
    main()