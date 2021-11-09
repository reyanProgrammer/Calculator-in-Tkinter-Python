from tkinter import *
from tkinter import font
import string
root = Tk()
# Event.widget.c


def split(word):
    return [char for char in word]


def action_click_NUM(event):
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        charNums = split(scvalue.get())
        alphabet_string = string.ascii_lowercase
        alphabet_list = list(alphabet_string)
        for char in charNums:
            for alphabet in alphabet_list:
                if char == alphabet:
                    scvalue.set("Error cannot add letters")
                    screen.update()
                    import time
                    time.sleep(2)
                    scvalue.set("")
                    screen.update()
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())

        scvalue.set(value)
    elif text == "c":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


root.geometry("455x577")
root.title("Calculator")
# print(font.families())
root.wm_iconbitmap('image.ico')

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvariable=scvalue, font=("Archivo Narrow", 16))
screen.pack(fill=X, padx=16, pady=6)

buttonsGroup1 = Frame(root, bg="#2a2b2a")
buttonsGroup1.pack()
b = Button(buttonsGroup1, text="9", font=('Sarala', 16), padx=16)
b.pack(side=LEFT, padx=12, pady=7)
b.bind("<Button-1>", action_click_NUM)
b1 = Button(buttonsGroup1, text="8", font=('Sarala', 16), padx=16)
b1.pack(side=LEFT, padx=12, pady=7)
b1.bind("<Button-1>", action_click_NUM)
b2 = Button(buttonsGroup1, text="7", font=('Sarala', 16), padx=16)
b2.pack(side=LEFT, padx=12, pady=7)
b2.bind("<Button-1>", action_click_NUM)
b3 = Button(buttonsGroup1, text="*", font=('Sarala', 16), padx=16)
b3.pack(side=LEFT, padx=12, pady=7)
b3.bind("<Button-1>", action_click_NUM)


buttonsGroup2 = Frame(root, bg="#2a2b2a")
buttonsGroup2.pack()

foutBut = Button(buttonsGroup2, text="4", font=('Sarala', 16), padx=16)
foutBut.pack(side=LEFT, padx=12, pady=7)
foutBut.bind("<Button-1>", action_click_NUM)

fiveBut = Button(buttonsGroup2, text="5", font=('Sarala', 16), padx=16)
fiveBut.pack(side=LEFT, padx=12, pady=7)
fiveBut.bind("<Button-1>", action_click_NUM)

sixBut = Button(buttonsGroup2, text="6", font=('Sarala', 16), padx=16)
sixBut.pack(side=LEFT, padx=12, pady=7)
sixBut.bind("<Button-1>", action_click_NUM)

minusBut = Button(buttonsGroup2, text="-", font=('Sarala', 16), padx=16)
minusBut.pack(side=LEFT, padx=12, pady=7)
minusBut.bind("<Button-1>", action_click_NUM)

buttonsGroup3 = Frame(root, bg="#2a2b2a")
buttonsGroup3.pack()

oneBut = Button(buttonsGroup3, text="1", font=('Sarala', 16), padx=16)
oneBut.pack(side=LEFT, padx=12, pady=7)
oneBut.bind("<Button-1>", action_click_NUM)

twoBut = Button(buttonsGroup3, text="2", font=('Sarala', 16), padx=16)
twoBut.pack(side=LEFT, padx=12, pady=7)
twoBut.bind("<Button-1>", action_click_NUM)

threeBut = Button(buttonsGroup3, text="3", font=('Sarala', 16), padx=16)
threeBut.pack(side=LEFT, padx=12, pady=7)
threeBut.bind("<Button-1>", action_click_NUM)

plusBut = Button(buttonsGroup3, text="+", font=('Sarala', 16), padx=16)
plusBut.pack(side=LEFT, padx=12, pady=7)
plusBut.bind("<Button-1>", action_click_NUM)

buttonsGroup4 = Frame(root, bg="#2a2b2a")
buttonsGroup4.pack()

clearBut = Button(buttonsGroup4, text="c", font=('Sarala', 16), padx=16)
clearBut.pack(side=LEFT, padx=12, pady=7)
clearBut.bind("<Button-1>", action_click_NUM)

equalBut = Button(buttonsGroup4, text="=", font=('Sarala', 16), padx=16)
equalBut.pack(side=LEFT, padx=12, pady=7)
equalBut.bind("<Button-1>", action_click_NUM)


divisionBut = Button(buttonsGroup4, text="/", font=('Sarala', 16), padx=16)
divisionBut.pack(side=LEFT, padx=12, pady=7)
divisionBut.bind("<Button-1>", action_click_NUM)
root.mainloop()
