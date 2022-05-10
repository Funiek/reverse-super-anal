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
encryption_frame = None
decryption_frame = None
files_frame = None
switch = 'generate_keys'


def frame_cleaner():
    global generate_keys_frame
    global encryption_frame
    global files_frame
    global switch

    if encryption_frame is not None:
        encryption_frame.destroy()
    if decryption_frame is not None:
        encryption_frame.destroy()
    if files_frame is not None:
        files_frame.destroy()
    if generate_keys_frame is not None:
        generate_keys_frame.destroy()


def init_generate_keys():
    global root
    global container_frame
    global switch
    global generate_keys_frame

    rsa_encryptor = RSAEncryptor()

    switch = 'generate_keys'
    frame_cleaner()
    
    generate_keys_frame = tk.Frame(container_frame)
    generate_keys_frame.pack(side=TOP,padx=(10,10),pady=(10,0))

    public_key_label = tk.Label(generate_keys_frame, text="Public key")
    public_key_label.pack(
        side=TOP,
        ipadx=5)
    
    public_key_text = tk.Text(generate_keys_frame, height=1, borderwidth=0)
    public_key_text.insert(1.0,"n: "+str(rsa_encryptor.encryptor.public_key.n)+" e: "+str(rsa_encryptor.encryptor.public_key.e))
    public_key_text.pack(
        side=TOP,
        ipadx=5)
    
    private_key_label = tk.Label(generate_keys_frame, text="Private key")
    private_key_label.pack(
        side=TOP,
        ipadx=5)

    private_key_text = tk.Text(generate_keys_frame, height=1, borderwidth=0)
    private_key_text.insert(1.0,"n: "+str(rsa_encryptor.encryptor.private_key.n)+" d: "+str(rsa_encryptor.encryptor.private_key.d))
    private_key_text.pack(
        side=TOP,
        ipadx=5)

    print("generate")


def init_encryption():
    global root
    global container_frame
    global switch
    global encryption_frame

    rsa_encryptor = RSAEncryptor()

    switch = 'encryption'
    frame_cleaner()

    encryption_frame = tk.Frame(container_frame)
    encryption_frame.pack(side=TOP,padx=(10,10),pady=(10,0))

    input_label = tk.Label(encryption_frame, text="Input value")
    input_label.pack(
        side=TOP,
        ipadx=5)
    
    input_text = tk.Text(encryption_frame, height=1, borderwidth=0)
    input_text.pack(
        side=TOP,
        ipadx=5)
    

    pub_k_n_label = tk.Label(encryption_frame, text="Public key \"n\"")
    pub_k_n_label.pack(
        side=TOP,
        ipadx=5)

    pub_k_n_text = tk.Text(encryption_frame, height=1, borderwidth=0)
    pub_k_n_text.pack(
        side=TOP,
        ipadx=5)

    pub_k_e_label = tk.Label(encryption_frame, text="Public key \"e\"")
    pub_k_e_label.pack(
        side=TOP,
        ipadx=5)

    pub_k_e_text = tk.Text(encryption_frame, height=1, borderwidth=0)
    pub_k_e_text.pack(
        side=TOP,
        ipadx=5)

    priv_k_n_label = tk.Label(encryption_frame, text="Private key \"n\"")
    priv_k_n_label.pack(
        side=TOP,
        ipadx=5)

    priv_k_n_text = tk.Text(encryption_frame, height=1, borderwidth=0)
    priv_k_n_text.pack(
        side=TOP,
        ipadx=5)

    priv_k_d_label = tk.Label(encryption_frame, text="Private key \"d\"")
    priv_k_d_label.pack(
        side=TOP,
        ipadx=5)

    priv_k_d_text = tk.Text(encryption_frame, height=1, borderwidth=0)
    priv_k_d_text.pack(
        side=TOP,
        ipadx=5)

    button = tk.Button(encryption_frame, text="Submit",
                             command=lambda: click(), width=80)
    button.pack(side=BOTTOM)

    output_text = tk.Text(encryption_frame, height=1, borderwidth=0)
    output_text.pack(
        side=BOTTOM,
        ipadx=5)

    output_label = tk.Label(encryption_frame, text="output value")
    output_label.pack(
        side=BOTTOM,
        ipadx=5)
    
    
    def click():
        value = input_text.get(1.0,'end-1c')
        
        n_pub = pub_k_n_text.get(1.0,'end-1c')
        e = pub_k_e_text.get(1.0,'end-1c')
        rsa_encryptor.encryptor.public_key.n=int(n_pub)
        rsa_encryptor.encryptor.public_key.e=int(e)

        n_priv = priv_k_n_text.get(1.0,'end-1c')
        d = priv_k_d_text.get(1.0,'end-1c')
        rsa_encryptor.encryptor.private_key.n=int(n_priv)
        rsa_encryptor.encryptor.private_key.d=int(d)

        encrypted = rsa_encryptor.encrypt_str(str(value))
        output_text.delete('1.0',END)
        output_text.insert(1.0,encrypted)

        print(str(rsa_encryptor.decrypt_str(encrypted)))


        
    
    print("encryption_button")

def init_decryption():
    global root
    global container_frame
    global switch
    global decryption_frame

    rsa_encryptor = RSAEncryptor()

    switch = 'decryption'
    frame_cleaner()

    decryption_frame = tk.Frame(container_frame)
    decryption_frame.pack(side=TOP,padx=(10,10),pady=(10,0))

    input_label = tk.Label(decryption_frame, text="Input value")
    input_label.pack(
        side=TOP,
        ipadx=5)
    
    input_text = tk.Text(decryption_frame, height=1, borderwidth=0)
    input_text.pack(
        side=TOP,
        ipadx=5)
    

    pub_k_n_label = tk.Label(decryption_frame, text="Public key \"n\"")
    pub_k_n_label.pack(
        side=TOP,
        ipadx=5)

    pub_k_n_text = tk.Text(decryption_frame, height=1, borderwidth=0)
    pub_k_n_text.pack(
        side=TOP,
        ipadx=5)

    pub_k_e_label = tk.Label(decryption_frame, text="Public key \"e\"")
    pub_k_e_label.pack(
        side=TOP,
        ipadx=5)

    pub_k_e_text = tk.Text(decryption_frame, height=1, borderwidth=0)
    pub_k_e_text.pack(
        side=TOP,
        ipadx=5)

    priv_k_n_label = tk.Label(decryption_frame, text="Private key \"n\"")
    priv_k_n_label.pack(
        side=TOP,
        ipadx=5)

    priv_k_n_text = tk.Text(decryption_frame, height=1, borderwidth=0)
    priv_k_n_text.pack(
        side=TOP,
        ipadx=5)

    priv_k_d_label = tk.Label(decryption_frame, text="Private key \"d\"")
    priv_k_d_label.pack(
        side=TOP,
        ipadx=5)

    priv_k_d_text = tk.Text(decryption_frame, height=1, borderwidth=0)
    priv_k_d_text.pack(
        side=TOP,
        ipadx=5)

    button = tk.Button(decryption_frame, text="Submit",
                             command=lambda: click(), width=80)
    button.pack(side=BOTTOM)

    output_text = tk.Text(decryption_frame, height=1, borderwidth=0)
    output_text.pack(
        side=BOTTOM,
        ipadx=5)

    output_label = tk.Label(decryption_frame, text="output value")
    output_label.pack(
        side=BOTTOM,
        ipadx=5)
    
    
    def click():
        value = str(input_text.get(1.0,'end-1c'))
        value = value.split()
        int_map = map(int, value)
        int_list = list(int_map)
        
        n_pub = pub_k_n_text.get(1.0,'end-1c')
        e = pub_k_e_text.get(1.0,'end-1c')
        rsa_encryptor.encryptor.public_key.n=int(n_pub)
        rsa_encryptor.encryptor.public_key.e=int(e)

        n_priv = priv_k_n_text.get(1.0,'end-1c')
        d = priv_k_d_text.get(1.0,'end-1c')
        rsa_encryptor.encryptor.private_key.n=int(n_priv)
        rsa_encryptor.encryptor.private_key.d=int(d)

        decrypted = rsa_encryptor.decrypt_str(int_list)
        output_text.delete('1.0',END)
        output_text.insert(1.0,decrypted)

        print(str(decrypted))


        
    
    print("decryption_button")


def init_files():
    global root
    global container_frame
    global switch
    global files_frame

    rsa_encryptor = RSAEncryptor()

    switch = 'files'
    frame_cleaner()
    
    files_frame = tk.Frame(container_frame)
    files_frame.pack(side=TOP,padx=(10,10),pady=(10,0))

    input_label = tk.Label(files_frame, text="Input path")
    input_label.pack(
        side=TOP,
        ipadx=5)
    
    input_text = tk.Text(files_frame, height=1, borderwidth=0)
    input_text.pack(
        side=TOP,
        ipadx=5)
    

    pub_k_n_label = tk.Label(files_frame, text="Public key \"n\"")
    pub_k_n_label.pack(
        side=TOP,
        ipadx=5)

    pub_k_n_text = tk.Text(files_frame, height=1, borderwidth=0)
    pub_k_n_text.pack(
        side=TOP,
        ipadx=5)

    pub_k_e_label = tk.Label(files_frame, text="Public key \"e\"")
    pub_k_e_label.pack(
        side=TOP,
        ipadx=5)

    pub_k_e_text = tk.Text(files_frame, height=1, borderwidth=0)
    pub_k_e_text.pack(
        side=TOP,
        ipadx=5)

    priv_k_n_label = tk.Label(files_frame, text="Private key \"n\"")
    priv_k_n_label.pack(
        side=TOP,
        ipadx=5)

    priv_k_n_text = tk.Text(files_frame, height=1, borderwidth=0)
    priv_k_n_text.pack(
        side=TOP,
        ipadx=5)

    priv_k_d_label = tk.Label(files_frame, text="Private key \"d\"")
    priv_k_d_label.pack(
        side=TOP,
        ipadx=5)

    priv_k_d_text = tk.Text(files_frame, height=1, borderwidth=0)
    priv_k_d_text.pack(
        side=TOP,
        ipadx=5)

    button = tk.Button(files_frame, text="Submit",
                             command=lambda: click(), width=80)
    button.pack(side=BOTTOM)

    output_text = tk.Text(files_frame, height=3, borderwidth=0)
    output_text.pack(
        side=BOTTOM,
        ipadx=5)

    output_label = tk.Label(files_frame, text="output value")
    output_label.pack(
        side=BOTTOM,
        ipadx=5)
    
    
    def click():
        n_pub = pub_k_n_text.get(1.0,'end-1c')
        e = pub_k_e_text.get(1.0,'end-1c')
        rsa_encryptor.encryptor.public_key.n=int(n_pub)
        rsa_encryptor.encryptor.public_key.e=int(e)

        n_priv = priv_k_n_text.get(1.0,'end-1c')
        d = priv_k_d_text.get(1.0,'end-1c')
        rsa_encryptor.encryptor.private_key.n=int(n_priv)
        rsa_encryptor.encryptor.private_key.d=int(d)

        path = str(input_text.get(1.0,'end-1c'))
        with open(path, 'rb') as file:
            value = file.read()

        en = rsa_encryptor.encrypt(value)
        print(en)

        de = rsa_encryptor.decrypt(en)
        print(de)

        new_path = path[0:path.find('.bin')] + ".result" + path[path.find('.bin'):]

        with open(new_path, 'wb+') as file:
            file.write(de)
        
        print(value)

        output_text.delete('1.0',END)
        output_text.insert(1.0,en)



def init():
    global root
    global container_frame

    root = tk.Tk()
    root.geometry("600x450")
    root.title("RSA Cipher")

    canvas = tk.Canvas(root, width=600, height=450, bg="#f9e8e9")
    canvas.pack()

    container_frame = tk.Frame(root, bg="#ffffff")
    container_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    buttons_frame = tk.Frame(container_frame, width=120, height=450)
    buttons_frame.pack(side=LEFT, anchor="w", pady=(40, 40))
    buttons_frame.pack_propagate(0)

    generate_keys_button = tk.Button(
        buttons_frame, text="Generate Keys", command=lambda: init_generate_keys(), width=120)
    generate_keys_button.pack(
        side=TOP
    )

    encryption_button = tk.Button(
        buttons_frame, text="Encryption", command=lambda: init_encryption(), width=120)
    encryption_button.pack(
        side=TOP
    )

    decryption_button = tk.Button(
        buttons_frame, text="Decryption", command=lambda: init_decryption(), width=120)
    decryption_button.pack(
        side=TOP
    )


    files_button = tk.Button(buttons_frame, text="File enc/dec",
                             command=lambda: init_files(), width=120)
    files_button.pack(
        side=TOP
    )

    init_generate_keys()

    root.mainloop()


if __name__ == "__main__":
    init()
