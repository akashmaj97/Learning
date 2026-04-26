import tkinter as tk
from tkinter import messagebox
import turtle   

window = tk.Tk()
window.title("My App")
window.minsize(300, 200)


tim = turtle.Turtle()
tim.speed(0)
tim.penup()
tim.goto(0, 0)
tim.pendown()
tim.write("Welcome to My App!", align="center", font=("Arial", 16, "bold"))

def show_message():
    messagebox.showinfo("Information", "Hello, Tkinter!")


tklabel = tk.Label(window, text="Welcome to My App!", font=("Arial", 16, "bold" ), fg="blue")
tklabel.pack(side=tk.TOP, pady=10) #add the label to the window at the center

button = tk.Button(window, text="Click Me", command=show_message)
button.pack(side=tk.BOTTOM, pady=10) #add the button to the window below the label

window.mainloop()