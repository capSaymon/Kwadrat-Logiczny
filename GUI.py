import tkinter as tk
from action import Run


llm = None
technique = None
sentence_A = None

color_main = '#303030'
color_button = "#1E688A"

button_style = {
    "width": 10,
    "height": 2,
    "bg": color_button,
    "fg": "white",
    "font": ("Helvetica", 12, "bold"),
    "bd": 0,
    "relief": "flat",
}

button_technique_style = {
    "width": 20,
    "height": 2,
    "bg": color_button,
    "fg": "white",
    "font": ("Helvetica", 12, "bold"),
    "bd": 0,
    "relief": "flat",
}


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

    center_frame = tk.Frame(page1, bg=color_main)
    center_frame.place(relx=0.5, rely=0.5, anchor="center")

    label1 = tk.Label(center_frame, text="Enter a sentence A:", bg=color_main, fg="white")
    label1.pack(pady=10)

    text_box = tk.Entry(center_frame, width=30, bg=color_main, fg="white", insertbackground="white")
    text_box.pack(pady=5)

    button_next = tk.Button(center_frame, text="Next", command=save_sentence_A, **button_style)
    button_next.pack(pady=10)

    page1.grid(row=0, column=0, sticky="nsew")


def page_choose_llm(container):
    global page2
    page2 = tk.Frame(container, width=600, height=550, bg=color_main)
    page2.grid_propagate(False)

    center_frame = tk.Frame(page2, bg=color_main)
    center_frame.place(relx=0.5, rely=0.5, anchor="center")

    list_llm: list[str] = ['gemini', 'llama', 'openai']

    for index, element in enumerate(list_llm):
        button_next = tk.Button(center_frame, text=element, command=lambda index=index: click_llm(index + 1), **button_style)
        button_next.pack(pady=10)

    page2.grid(row=0, column=0, sticky="nsew")


def page_choose_technique(container):
    global page3
    page3 = tk.Frame(container, width=600, height=550, bg=color_main)
    page3.grid_propagate(False)

    center_frame = tk.Frame(page3, bg=color_main)
    center_frame.place(relx=0.5, rely=0.5, anchor="center")

    list_llm: list[str] = ['zero-shot', 'one-shot', 'few-shot', 'self-consistency', 'chain-of-thought', 'ReAct']
    if llm == 2:
        list_llm.append('HyDE')

    for index, element in enumerate(list_llm):
        button_next = tk.Button(center_frame, text=element, command=lambda index=index: click_technique(index), **button_technique_style)
        button_next.pack(pady=10)

    page3.grid(row=0, column=0, sticky="nsew")


def page_generate_sentences(container):
    global page4, label1
    page4 = tk.Frame(container, width=600, height=550, bg=color_main)
    page4.grid_propagate(False)

    center_frame = tk.Frame(page4, bg=color_main)
    center_frame.place(relx=0.5, rely=0.5, anchor="center")

    def update_outcome():
        print('\nGenerate new outcome')
        new_outcome = generate_sentences()
        label1.config(text=new_outcome)

    outcome = generate_sentences()
    label1 = tk.Label(center_frame, text=outcome, bg=color_main, fg="white", wraplength=500, justify="left")
    label1.pack(pady=10)

    button_save = tk.Button(center_frame, text="Save", command=lambda: save_result(outcome), **button_style)
    button_save.pack(pady=10)

    button_reject = tk.Button(center_frame, text="Reject", command=update_outcome, **button_style)
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
