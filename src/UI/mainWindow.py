from glob import glob
import os
import tkinter as tk
from tkinter import BOTTOM, CENTER, LEFT, N, NW, RIGHT, TOP, Canvas, filedialog, Text
from tkinter import *
from tkinter.ttk import *
from RSAEncryptor.RSAEncryptor import RSAEncryptor

root = None
container_frame = None
generate_keys_frame = None
encryption_decryption_frame = None
files_frame = None
switch = 'generate_keys'
rsa_encryptor = RSAEncryptor()

def frame_cleaner():
    global generate_keys_frame
    global encryption_decryption_frame
    global files_frame
    global switch

    if encryption_decryption_frame is not None:
        encryption_decryption_frame.destroy()
    if files_frame is not None:
        files_frame.destroy()
    if generate_keys_frame is not None:
        generate_keys_frame.destroy()


def init_generate_keys():
    global root
    global container_frame
    global switch
    global generate_keys_frame

    switch = 'generate_keys'
    frame_cleaner()

    generate_keys_frame = tk.Frame(container_frame)
    generate_keys_frame.pack(side=TOP,pady=(10,0))

    public_key_label = tk.Label(generate_keys_frame, text="Public key")
    public_key_label.pack(
        side=TOP,
        ipadx=5)
    
    public_key_text = tk.Text(generate_keys_frame, height=1, borderwidth=0)
    public_key_text.insert(1.0,rsa_encryptor.encryptor.public_key)

    print("generate")


def init_encryption_decryption():
    global root
    global container_frame
    global switch
    global encryption_decryption_frame

    switch = 'encryption_decryption'
    frame_cleaner()

    encryption_decryption_frame = tk.Frame(container_frame)
    encryption_decryption_frame.pack(side=TOP,pady=(10,0))

    public_key_label = tk.Label(encryption_decryption_frame, text="Input")
    public_key_label.pack(
        side=TOP,
        ipadx=5)
    
    print("encryption_decryption_button")


def init_files():
    global root
    global container_frame
    global switch
    global files_frame

    switch = 'files'
    frame_cleaner()

    files_frame = tk.Frame(container_frame)
    files_frame.pack(side=TOP,pady=(10,0))

    public_key_label = tk.Label(files_frame, text="File real path")
    public_key_label.pack(
        side=TOP,
        ipadx=5)
    
    print("files")


def init():
    global root
    global container_frame

    root = tk.Tk()
    root.geometry("600x200")
    root.title("RSA Cipher")

    canvas = tk.Canvas(root, width=600, height=200, bg="#f9e8e9")
    canvas.pack()

    container_frame = tk.Frame(root, bg="#ffffff")
    container_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    buttons_frame = tk.Frame(container_frame, width=120, height=150)
    buttons_frame.pack(side=LEFT, anchor="w", pady=(40, 40))
    buttons_frame.pack_propagate(0)

    generate_keys_button = tk.Button(
        buttons_frame, text="Generate Keys", command=lambda: init_generate_keys(), width=120)
    generate_keys_button.pack(
        side=TOP
    )

    encryption_decryption_button = tk.Button(
        buttons_frame, text="Encryption", command=lambda: init_encryption_decryption(), width=120)
    encryption_decryption_button.pack(
        side=TOP
    )

    files_button = tk.Button(buttons_frame, text="Files",
                             command=lambda: init_files(), width=120)
    files_button.pack(
        side=TOP
    )

    init_generate_keys()

    root.mainloop()


if __name__ == "__main__":
    init()
