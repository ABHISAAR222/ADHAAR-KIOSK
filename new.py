import cv2
import time
import datetime as dt
import argparse
import tkinter as tk
from tkinter import *
from tkinter.font import BOLD
from turtle import width
from matplotlib.pyplot import title
from numpy import place
from pip import main
from tkinter import Button, messagebox
from PIL import Image, ImageTk
from tkcalendar import Calendar, DateEntry
root = tk.Tk()
root.title('ADHAAR KIOSK')
root.geometry('1280x720')
label = Label(root, text="AADHAAR KIOSK", font=(
    'comic sans', 40, 'bold'), fg="red", bg="white")
label.pack()
label1 = Label(root, text="Choose Your Preferred Language /",
               font=('comic sans', 20, 'bold'), fg="red", bg="white")
label1.pack()
label2 = Label(root, text="अपनी पसंदीदा भाषा चुनें", font=(
    'comic sans', 20, 'bold'), fg="red", bg="white")
label2.pack()


def english():
    global my_img
    top = Toplevel()
    root.geometry('1280x720')
    top.title('new user')
    top.iconbitmap('logo.png')
    Button(top, text="NEW USER REGISTRATION", font=("comic sans", 30),
           fg="green", bg="white", width=30, height=0, command=register).pack()
    Button(top, text="LOGIN", font=("comic sans", 40), fg="green",
           bg="white", width=25, height=0, command=login).pack()


def open():
    global my_img
    root = tk.Tk()
    top = Toplevel()
    root.geometry('1280x720')
    top.title('ENGLISH')
    top.iconbitmap('logo.png')


btn = Button(root, text="ENGLISH", font=("comic sans", 40),
             fg="green", bg="white", width=20, height=0, command=english).pack()


def open1():
    global my_img
    root = tk.Tk()
    top = Toplevel()
    root.geometry('1280x720')
    top.title('HINDI')
    top.iconbitmap('logo.png')


btn = Button(root, text="HINDI", font=("comic sans", 40), fg="green",
             bg="white", width=20, height=0, command=open1).pack()


def register():
    root = tk.Tk()
    top = Toplevel()
    root.geometry('1280x720')
    root.title("Register")
    top.iconbitmap('logo.png')

    root.configure(bg="pink")

    l1 = tk.Label(root, text="Mobile no:", font=(
        "Arial", 15), bg="pink")
    l1.place(x=10, y=10)
    t1 = tk.Entry(root, width=30, bd=5)
    t1.place(x=200, y=10)

    l2 = tk.Label(root, text="otp:", font=(
        "Arial", 15), bg="pink")
    l2.place(x=10, y=60)
    t2 = tk.Entry(root, width=30, show="*", bd=5)
    t2.place(x=200, y=60)

    def check():
        if t1.get() != "" or t2.get() != "":
            if t1.get() != t2.get():
                messagebox.showinfo(
                    "Welcome", "You are registered successfully!!")
            else:
                messagebox.showinfo("Error")
        else:
            messagebox.showinfo("Error", "Please fill the complete field!!")

    b1 = tk.Button(root, text="Sign in", font=("Arial", 15),
                   bg="#ffc22a", command=main_window)
    b1.place(x=170, y=190)


def main_window():
    root = tk.Tk()
    top = Toplevel()
    root.geometry('1280x720')
    root.title("Enrollement page")
    top.iconbitmap('logo.png')

    root.configure(bg="pink")

    label = Label(root, text="Enrollment page-1", font=(
        'comic sans', 40, 'bold'), fg="red", bg="white")
    label.pack()
    l1 = tk.Label(root, text="First Name:", font=(
        "Arial", 15), bg="pink")
    l1.place(x=10, y=360)
    t1 = tk.Entry(root, width=30, bd=5)
    t1.place(x=200, y=360)

    l2 = tk.Label(root, text="Middle name:", font=(
        "Arial", 15), bg="pink")
    l2.place(x=10, y=400)
    t2 = tk.Entry(root, width=30, bd=5)
    t2.place(x=200, y=400)

    l3 = tk.Label(root, text="Last name:", font=(
        "Arial", 15), bg="pink")
    l3.place(x=10, y=440)
    t3 = tk.Entry(root, width=30, bd=5)
    t3.place(x=200, y=440)
    l4 = tk.Label(root, text="Date of birth:", font=(
        "Arial", 15), bg="pink")
    l4.place(x=10, y=480)
    cal = DateEntry(root, width=16, background="magenta3",
                    foreground="white", bd=2)
    cal.place(x=250, y=480)
    l5 = tk.Label(root, text="Gender:", font=(
        "Arial", 15), bg="pink")
    l5.place(x=10, y=520)
    t5 = tk.Entry(root, width=30, bd=5)
    t5.place(x=200, y=520)
    l5 = tk.Label(root, text="Address:", font=(
        "Arial", 15), bg="pink")
    l5.place(x=10, y=560)
    t5 = tk.Entry(root, width=30, bd=5)
    t5.place(x=200, y=560)
    l5 = tk.Label(root, text="Contact no:", font=(
        "Arial", 15), bg="pink")
    l5.place(x=10, y=600)
    t5 = tk.Entry(root, width=30, bd=5)
    t5.place(x=200, y=600)
    b1 = tk.Button(root, text="Next Page", font=(
        "Arial", 15), bg="#ffc22a", command=next_page)
    b1.place(x=650, y=600)


def next_page():
    root = tk.Tk()
    top = Toplevel()
    root.geometry('1280x720')
    root.title("Documents upload page")
    top.iconbitmap('logo.png')

    root.configure(bg="pink")
    label = Label(root, text="Documents Upload page ", font=(
        'comic sans', 40, 'bold'), fg="red", bg="white")
    label.pack()
    l1 = tk.Label(root, text="Date of birth proof :", font=(
        "Arial", 15), bg="pink")
    l1.place(x=10, y=100)
    clicked = StringVar()
    clicked.set("10TH MARKSHEET")
    drop = OptionMenu(root, clicked, "10TH MARKSHEET",
                      "DATE OF BIRTH CERFICATE")
    drop.place(x=180, y=100)
    drop.config(width=20)
    l2 = tk.Label(root, text="ADDRESS PROOF :", font=(
        "Arial", 15), bg="pink")
    l2.place(x=10, y=200)
    clicked1 = StringVar()
    clicked1.set("Electricity Bill")
    drop1 = OptionMenu(root, clicked1, "Electricity Bill")
    drop1.place(x=200, y=200)
    drop1.config(width=20)
    b1 = tk.Button(root, text="Next Page", font=(
        "Arial", 15), bg="#ffc22a", command=next_page2)
    b1.place(x=650, y=600)

def next_page2():
    root = tk.Tk()
    top = Toplevel()
    root.geometry('1280x720')
    root.title("BIOMETRICS PAGE")
    top.iconbitmap('logo.png')
    label = Label(root, text="Biometrics page", font=(
    'comic sans', 40, 'bold'), fg="red", bg="white")
    label.pack()

def login():
    root = tk.Tk()
    top = Toplevel()
    root.geometry('1280x720')
    root.title("BIOMETRICS PAGE")
    top.iconbitmap('logo.png')
    label = Label(root, text="LOGIN PAGE", font=(
    'comic sans', 40, 'bold'), fg="red", bg="white")
    label.pack()
    l1 = tk.Label(root, text="NAME:", font=(
        "Arial", 15), bg="pink")
    l1.place(x=10, y=300)
    t1 = tk.Entry(root, width=30, bd=5)
    t1.place(x=200, y=300)
    l1 = tk.Label(root, text="ADHAAR LINKED Mobile no:", font=(
        "Arial", 15), bg="pink")
    l1.place(x=10, y=340)
    t1 = tk.Entry(root, width=30, bd=5)
    t1.place(x=300, y=340)

    l2 = tk.Label(root, text="otp:", font=(
        "Arial", 15), bg="pink")
    l2.place(x=10, y=380)
    t2 = tk.Entry(root, width=30, show="*", bd=5)
    t2.place(x=200, y=380)
    b1 = tk.Button(root, text="Sign in", font=("Arial", 15),
                   bg="#ffc22a", command=updation)
    b1.place(x=170, y=500)
def updation():
        root = tk.Tk()
        top = Toplevel()
        root.geometry('1280x720')
        root.title("BIOMETRICS PAGE")
        top.iconbitmap('logo.png')
        label = Label(root, text="Details and biometric updation page", font=(
        'comic sans', 40, 'bold'), fg="red", bg="white")
        label.pack()

mainloop()
