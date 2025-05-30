import tkinter as tk


def save_sentence_A():
    global sentence_A
    sentence_A = text_box.get()
    label2.config(text=sentence_A)
    print("Zapisano do zmiennej:", sentence_A)
    show_frame(page2)

def show_frame(frame):
    frame.tkraise()

def page1_view(container):
    global text_box, page1
    page1 = tk.Frame(container, width=600, height=550)
    page1.grid_propagate(False)

    center_frame = tk.Frame(page1)
    center_frame.place(relx=0.5, rely=0.5, anchor="center")

    label1 = tk.Label(center_frame, text="Wpisz zdanie A:")
    label1.pack(pady=10)

    text_box = tk.Entry(center_frame, width=30)
    text_box.pack(pady=5)

    button_next = tk.Button(center_frame, text="Dalej", command=save_sentence_A)
    button_next.pack(pady=10)

    page1.grid(row=0, column=0, sticky="nsew")

def page2_view(container):
    global page2, label2
    page2 = tk.Frame(container, width=600, height=550)
    page2.grid_propagate(False)

    center_frame = tk.Frame(page2)
    center_frame.place(relx=0.5, rely=0.5, anchor="center")

    label2 = tk.Label(center_frame, text='')
    label2.pack(pady=20)

    button_back = tk.Button(center_frame, text="Wróć", command=lambda: show_frame(page1))
    button_back.pack()

    page2.grid(row=0, column=0, sticky="nsew")

def main():
    global window
    window = tk.Tk()
    window.title("Kwadrat Logiczny")

    width = 600
    height = 550
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

    container = tk.Frame(window)
    container.pack(fill="both", expand=True)

    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)

    page1_view(container)
    page2_view(container)
    show_frame(page1)

    window.mainloop()

if __name__ == "__main__":
    main()
