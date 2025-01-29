import tkinter

def main(window: tkinter.Tk):
    window.title("minecraft calculator v1")

    add_label(window, 'What items do you want to make?')

    window.mainloop()

def add_label(window, text):
    text_label = tkinter.Label(window, text=text)
    text_label.pack()

main(tkinter.Tk())
