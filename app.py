import tkinter
from tkinter import ttk

iron_needed: int = 0

def main(window: tkinter.Tk):
    window.title("minecraft calculator v1")
    window.geometry("854x480")

    frame = ttk.Frame(window, padding=10)
    frame.grid()

    label = ttk.Label(frame, text="What items do you want to make?")
    label.grid(row=0, column=0)

    btn = ttk.Button(frame, text="Hopper", command=lambda: add_iron(5))
    btn.grid(row=1, column=0)
    btn = ttk.Button(frame, text="Anvil", command=lambda: add_iron(30))
    btn.grid(row=1, column=1)

    window.mainloop()

def add_iron(amount: int):
    global iron_needed
    iron_needed += amount
    print(f"you need {iron_needed} iron ingots")

main(tkinter.Tk())
