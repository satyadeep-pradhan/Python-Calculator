# import tkinter module
from tkinter import *

# import other necessary modules
import random

import base64

# creating root object
root = Tk()

# defining size of window
root.geometry("700x2500")

# setting up the title of window
root.title("Encryption and Decryption of message")

Tops = Frame(root, width=1600, relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=800, relief=SUNKEN)
f1.pack(side=LEFT)




lblInfo = Label(Tops, font=('cambria', 26, 'bold'),
                text="Sat's Encryption and Decryption",
                fg="Black", bd=10, anchor='w')

lblInfo.grid(row=1, column=0)


# Initializing variables
Msg = StringVar()
key = StringVar()
mode = StringVar()
Result = StringVar()


# labels for the message
lblMsg = Label(f1, font=('cambria', 15, 'bold'),
               text="MESSAGE\n", bd=16, anchor="w")

lblMsg.grid(row=1, column=1)
# Entry box for the message
txtMsg = Entry(f1, font=('cambria', 15, 'bold'),
               textvariable=Msg, bd=16, insertwidth=4,
               bg="lightgrey", justify='right')


txtMsg.grid(row=1, column=2)
# labels for the key
lblkey = Label(f1, font=('cambria', 15, 'bold'),
               text="KEY (Only Integer)", bd=16, anchor="w")

lblkey.grid(row=2, column=1)


# Entry box for the key
txtkey = Entry(f1, font=('cambria', 15, 'bold'),
               textvariable=key, bd=16, insertwidth=4,
               bg="lightgrey", justify='right')

txtkey.grid(row=2, column=2)

# labels for the mode
lblmode = Label(f1, font=('cambria', 15, 'bold'),
                text="MODE\n(e for encrypt) \n (d for decrypt)",
                bd=16, anchor="w")

lblmode.grid(row=3, column=1)
# Entry box for the mode
txtmode = Entry(f1, font=('cambria', 15, 'bold'),
                textvariable=mode, bd=15, insertwidth=4,
                bg="lightgrey", justify='right')

txtmode.grid(row=3, column=2)

# labels for the result
lblResult = Label(f1, font=('cambria', 15, 'bold'),
                  text="\n",
                   bd=16, anchor="w")

lblResult.grid(row=7, column=1)

# Making of Entry box for the result
txtResult = Entry(f1, font=('cambria', 15, 'bold'),
                  textvariable=Result, bd=15, insertwidth=4,
                  bg="lightgrey", justify='right')

txtResult.grid(row=7, column=2)

# function to encode

def encode(key, msg):
    enc = []
    for i in range(len(msg)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(msg[i]) +
                     ord(key_c)) % 256)
        enc.append(enc_c)
        print("enc:", enc)
    enc_text = base64.urlsafe_b64encode("".join(enc).encode()).decode()
    with open("enc_text", 'a+') as f:
        f.write(enc_text + "\n")
    return enc_text


# Function to decode


def decode(key, enc):
    dec = []

    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) -
                     ord(key_c)) % 256)

        dec.append(dec_c)
        print("dec:", dec)
    return "".join(dec)


def Results():
    # print("Message= ", (Msg.get()))

    msg = Msg.get()
    k = key.get()
    m = mode.get()

    if (m == 'e'):
        Result.set(encode(k, msg))
    else:
        Result.set(decode(k, msg))

# exit function

def qExit():
    root.destroy()

def Reset():

    Msg.set("")
    key.set("")
    mode.set("")
    Result.set("")

# Show message button
btnTotal = Button(f1, padx=15, pady=5, bd=5, fg="black",
                  font=('cambria', 15, 'bold'), width=10,
                  text="Show Message", bg="#90EE90",
                  command=Results).grid(row=4, column=2)
# Reset button
btnReset = Button(f1, padx=13, pady=5, bd=13,
                  fg="black", font=('cambria', 15, 'bold'),
                  width=10, text="Reset", bg="#356093",
                  command=Reset).grid(row=10, column=1)

# Exit button
btnExit = Button(f1, padx=13, pady=5, bd=13,
                 fg="black", font=('cambria', 15, 'bold'),
                 width=10, text="Exit", bg="#FF7F7F",
                 command=qExit).grid(row=10, column=10)





root.mainloop()