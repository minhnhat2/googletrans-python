from tkinter import *
from PIL import Image, ImageTk
import googletrans
from tkinter import filedialog

#tạo giao diện
root = Tk()
root.title('Manchester United')  
root.geometry("500x630")
root.iconbitmap('manchesterunited.ico')

load = Image.open('a.jpg')
render = ImageTk.PhotoImage(load)
img = Label(root, image=render)
img.place(x=0, y=0)

name = Label(root, text="Translate", fg="#FFFFFF", bd=0, bg="#02142C")
name.config(font=("Translate vietnamese", 30))
name.pack(pady=10)

box = Text(root, width=28, height=8, font=("ROBOTO", 16))
box.pack(pady=20)

button_frame = Frame(root).pack(side=BOTTOM)

def clear():
    box.delete(1.0, END)
    box1.delete(1.0, END)

def translate():
    text = box.get(1.0, END)
    translator = googletrans.Translator()
    translated_text = translator.translate(text, dest='vi').text
    box1.insert(END, translated_text)

def reverse_translate():
    text = box1.get(1.0, END)
    translator = googletrans.Translator()
    translated_text = translator.translate(text, dest='en').text
    box.insert(END, translated_text)

def load_file():
    file_path = filedialog.askopenfilename()
    with open(file_path, 'r') as f:
        text = f.read()
    box.insert(END, text)

clear_button = Button(button_frame, text="Clear text", font=(("Arial"), 10, 'bold'), bg='#303030', fg="#FFFFFF", command=clear)
clear_button.place(x=150, y=310)
trans_button = Button(button_frame, text="Translate", font=(("Arial"), 10, 'bold'), bg='#303030', fg="#FFFFFF", command=translate)
trans_button.place(x=290, y=310)
reverse_button = Button(button_frame, text="Reverse translate", font=(("Arial"), 10, 'bold'), bg='#303030', fg="#FFFFFF", command=reverse_translate)
reverse_button.place(x=10, y=310)
load_button = Button(button_frame, text="Load file", font=(("Arial"), 10, 'bold'), bg='#303030', fg="#FFFFFF", command=load_file)
load_button.place(x=430, y=310)

box1 = Text(root, width=28, height=8, font=("ROBOTO", 16))
box1.pack(pady=50)

root.mainloop()
