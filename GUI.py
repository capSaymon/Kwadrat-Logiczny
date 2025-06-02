from decorations import color_main, color_decorate, color_input, text_enter, text_input, text_style, button_style, button_technique_style
from action import Run
import tkinter as tk


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
    page1 = tk.Frame(container, width=600, height=550, bg=color_main)
    page1.grid_propagate(False)

    center_frame = tk.Frame(page1, bg=color_main, width=400, height=250)
    center_frame.place(relx=0.5, rely=0.5, anchor="center")
    center_frame.pack_propagate(False)

    input_frame = tk.Frame(center_frame, bg=color_decorate)
    input_frame.pack(pady=10, fill='x', expand=True)

    label1 = tk.Label(input_frame, text="Enter a sentence A:", bg=color_decorate, **text_enter)
    label1.pack(pady=(10, 5))

    text_box = tk.Entry(input_frame, width=40, insertbackground="white", bd=0, relief="flat", bg=color_input, **text_input)
    text_box.pack(pady=(0, 10), ipady=10)

    button_next = tk.Button(center_frame, text="Next", command=save_sentence_A, **button_style)
    button_next.pack(pady=(30, 10))

    page1.grid(row=0, column=0, sticky="nsew")




def page_choose_llm(container):
    global page2
    page2 = tk.Frame(container, width=600, height=550, bg=color_main)
    page2.grid_propagate(False)

    center_frame = tk.Frame(page2, bg=color_main)
    center_frame.place(relx=0.5, rely=0.5, anchor="center")

    label1 = tk.Label(center_frame, text="Select LLM", **text_style)
    label1.grid(row=0, column=0, columnspan=3, pady=(0, 50))

    list_llm: list[str] = ['gemini', 'llama', 'openai']

    for index, element in enumerate(list_llm):
        button_llm = tk.Button(center_frame, text=element, command=lambda index=index: click_llm(index + 1), **button_style)
        button_llm.grid(row=1, column=index, padx=10)

    page2.grid(row=0, column=0, sticky="nsew")


def page_choose_technique(container):
    global page3
    page3 = tk.Frame(container, width=600, height=550, bg=color_main)
    page3.grid_propagate(False)

    center_frame = tk.Frame(page3, bg=color_main)
    center_frame.place(relx=0.5, rely=0.5, anchor="center")

    label1 = tk.Label(center_frame, text="Select prompt technique", **text_style)
    label1.grid(row=0, column=0, columnspan=3, pady=(0, 50))

    list_llm: list[str] = ['zero-shot', 'one-shot', 'few-shot', 'self-consistency', 'chain-of-thought', 'ReAct']

    for index, element in enumerate(list_llm):
        row = index // 2 + 1
        col = index % 2
        button_technique = tk.Button(center_frame, text=element, command=lambda index=index: click_technique(index), **button_technique_style)
        button_technique.grid(row=row, column=col, padx=10, pady=10)
    
    if llm == 2:
        index_hyde = len(list_llm)
        button_technique = tk.Button(center_frame, text="HyDE", command=lambda: click_technique(index_hyde), **button_technique_style)
        button_technique.grid(row=row + 1, column=0, columnspan=2, pady=(10, 0))

    page3.grid(row=0, column=0, sticky="nsew")


def page_generate_sentences(container):
    global page4
    page4 = tk.Frame(container, width=600, height=550, bg=color_main)
    page4.grid_propagate(False)

    center_frame = tk.Frame(page4, bg=color_main)
    center_frame.place(relx=0.5, rely=0.5, anchor="center")

    outcome_var = tk.StringVar()
    outcome_var.set(generate_sentences())

    label_title = tk.Label(center_frame, text="The rest of the sentences", **text_style)
    label_title.grid(row=0, column=0, columnspan=3, pady=(0, 30))

    label1 = tk.Label(center_frame, textvariable=outcome_var, wraplength=500, justify='left',
                      **text_style, background=color_decorate, padx=20, pady=20)
    label1.grid(row=1, column=0, columnspan=2, pady=0)

    def update_outcome():
        print('\nGenerate new outcome')
        outcome_var.set(generate_sentences())

    def save_current_result():
        save_result(outcome_var.get())

    button_save = tk.Button(center_frame, text="Save", command=save_current_result, **button_style)
    button_save.grid(row=2, column=0, padx=30, pady=50)

    button_reject = tk.Button(center_frame, text="Reject", command=update_outcome, **button_style)
    button_reject.grid(row=2, column=1, padx=30, pady=50)

    page4.grid(row=0, column=0, sticky="nsew")




def main():
    global window, container
    window = tk.Tk()
    window.title("Logical Square")

    width = 700
    height = 650
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")
    window.configure(bg=color_main)

    container = tk.Frame(window, bg=color_main)
    container.pack(fill="both", expand=True)

    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)

    page_input_sentence(container)
    page_choose_llm(container)
    show_frame(page1)

    window.mainloop()


if __name__ == "__main__":
    main()
