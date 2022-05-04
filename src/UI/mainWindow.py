import tkinter as tk


def init():
    window = tk.Tk()
    window.geometry("600x400")
    window.title("RSA Cipher")
    window.config(bg="#ff00ff")

    container_frame = tk.Frame(window, width=400, height=300)
    container_frame.pack()

    input_label = tk.Label(container_frame, text="Input")
    input_label.pack(side=tk.TOP)

    window.mainloop()


if __name__ == "__main__":
    init()
