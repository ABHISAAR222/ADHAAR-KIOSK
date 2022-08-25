import tkinter as tk
from PIL import Image
import pyttsx3
import speech_recognition as sr
root = tk.Tk()
root.geometry('1920x1080')
root.configure(bg='#1974D2')
file="D:\sih\python scripts\\2.gif"
label =tk.Label(root, text="Iris Scanner", font=(
    'comic sans', 60, 'bold'), fg="black", bg="white")
label.pack()
info = Image.open(file)

frames = info.n_frames 

im = [tk.PhotoImage(file=file,format=f"gif -index {i}") for i in range(frames)]

def speak(text):
    engine = pyttsx3.init()
    engine.say("hello")
    engine.runAndWait()
count = 0
anim = None
def animation(count):
    global anim
    im2 = im[count]

    gif_label.configure(image=im2)
    count += 1
    if count == frames:
        count = 0
    anim = root.after(50,lambda :animation(count))

def stop_animation():
    root.after_cancel(anim)

gif_label = tk.Label(root,image="")
gif_label.pack()

start = tk.Button(root,text="start",command=lambda :animation(count))
start.pack()

root.mainloop()