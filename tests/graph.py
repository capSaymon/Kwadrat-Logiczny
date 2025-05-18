import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import glob
import os

def data_result(file_name: str = ''):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    file_path = glob.glob(os.path.join(BASE_DIR, f'{file_name}.csv'))
    if not file_path:
        raise FileNotFoundError("file not found")

    df = pd.read_csv(file_path[0])
    metrics = ['Attempts', 'Format Success', 'Relation Success', 'First Aproach Successful']
    grouped = df.groupby('Question')

    questions = []
    data = {metric: [] for metric in metrics}

    print('=' * 50)
    print(f"{file_name}\nValues for questions:\n")
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
    ax.set_title(f'{file_name}')
    ax.set_xticks(x)
    ax.set_xticklabels(questions, rotation=45, ha='right')
    ax.legend()

    plt.tight_layout()
    plt.show()



def main():
    data_result('report_LLAMA')
    data_result('report_HyDE')

if __name__ == '__main__':
    main()