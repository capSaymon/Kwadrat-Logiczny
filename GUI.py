import tkinter as tk
from action import Run


llm = None
technique = None
sentence_A = None


def save_sentence_A():
    global sentence_A
    sentence_A = text_box.get()
    if sentence_A:
        show_frame(page2)
        print("Saved to variable: ", sentence_A)


def click_llm(index):
    global llm
    llm = index
    print(f"Selected LLM: {llm}")
    page_choose_technique(container)
    show_frame(page3)


def click_technique(index):
    global technique
    technique = index
    print(f"Selected technique: {technique}")
    page_generate_sentences(container)
    show_frame(page4)


def generate_sentences() -> str:
    action = Run('A: '+sentence_A, llm, technique)
    outcome = action.result()
    return outcome

def save_result(outcome):
    action = Run()
    print('Accept answear and save\n')
    action.save(outcome)


def show_frame(frame):
    frame.tkraise()


def page_input_sentence(container):
    global text_box, page1
    page1 = tk.Frame(container, width=600, height=550)
    page1.grid_propagate(False)

    center_frame = tk.Frame(page1)
    center_frame.place(relx=0.5, rely=0.5, anchor="center")

    label1 = tk.Label(center_frame, text="Enter a sentence A:")
    label1.pack(pady=10)

    text_box = tk.Entry(center_frame, width=30)
    text_box.pack(pady=5)

    button_next = tk.Button(center_frame, text="Next", command=save_sentence_A)
    button_next.pack(pady=10)

    page1.grid(row=0, column=0, sticky="nsew")


def page_choose_llm(container):
    global page2
    page2 = tk.Frame(container, width=600, height=550)
    page2.grid_propagate(False)

    center_frame = tk.Frame(page2)
    center_frame.place(relx=0.5, rely=0.5, anchor="center")

    list_llm: list[str] = ['gemini', 'llama', 'openai']

    for index, element in enumerate(list_llm):
        button_next = tk.Button(center_frame, text=element, command=lambda index=index: click_llm(index+1))
        button_next.pack(pady=10)

    page2.grid(row=0, column=0, sticky="nsew")


def page_choose_technique(container):
    global page3
    page3 = tk.Frame(container, width=600, height=550)
    page3.grid_propagate(False)

    center_frame = tk.Frame(page3)
    center_frame.place(relx=0.5, rely=0.5, anchor="center")

    list_llm: list[str] = ['zero-shot', 'one-shot', 'few-shot', 'self-consistency', 'chain-of-thought', 'ReAct']
    if llm == 2:
        list_llm.append('HyDE')

    for index, element in enumerate(list_llm):
        button_next = tk.Button(center_frame, text=element, command=lambda index=index: click_technique(index))
        button_next.pack(pady=10)

    page3.grid(row=0, column=0, sticky="nsew")


def page_generate_sentences(container):
    global page4, label1
    page4 = tk.Frame(container, width=600, height=550)
    page4.grid_propagate(False)

    center_frame = tk.Frame(page4)
    center_frame.place(relx=0.5, rely=0.5, anchor="center")

    def update_outcome():
        print('\nGenerate new outcome')
        new_outcome = generate_sentences()
        label1.config(text=new_outcome)

    outcome = generate_sentences()
    label1 = tk.Label(center_frame, text=outcome)
    label1.pack(pady=10)

    button_save = tk.Button(center_frame, text="Save", command=lambda: save_result(outcome))
    button_save.pack(pady=10)

    button_reject = tk.Button(center_frame, text="Reject", command=update_outcome)
    button_reject.pack(pady=10)

    page4.grid(row=0, column=0, sticky="nsew")



def main():
    global window, container
    window = tk.Tk()
    window.title("Logical Square")

    width = 600
    height = 550
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

    container = tk.Frame(window)
    container.pack(fill="both", expand=True)

    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)

    page_input_sentence(container)
    page_choose_llm(container)
    show_frame(page1)

    window.mainloop()


if __name__ == "__main__":
    main()
