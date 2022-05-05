from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Tic Tac Toe")
#window.geometry("300x300")
window.configure(bg="#d9b2cf")

winner = False
clicked_button = True
count = 0
b1 = StringVar()
b1.set("")
b2 = StringVar()
b2.set("")
b3 = StringVar()
b3.set("")
b4 = StringVar()
b4.set("")
b5 = StringVar()
b5.set("")
b6 = StringVar()
b6.set("")
b7 = StringVar()
b7.set("")
b8 = StringVar()
b8.set("")
b9 = StringVar()
b9.set("")
x_player = IntVar()
x_player.set(0)
o_player = IntVar()
o_player.set(0)


Xplayer = Label(text="Player1: X")
Xplayer.grid(row=0, column=0, columnspan=1)
Oplayer = Label(text="Player2: O")
Oplayer.grid(row=0, column=2, columnspan=2,padx=10)
Xplayer_label = Label(textvariable=x_player)
Xplayer_label.grid(row=1, column=0)
Oplayer_label = Label(textvariable=o_player)
Oplayer_label.grid(row=1, column=2)


def clicked():
    global clicked_button,count
    if clicked_button == True:
        clicked_button = False
        return "X"
    elif clicked_button==False:
        clicked_button=True
        return "O"

def clicked1():
    global clicked_button,count
    if b1.get()=="":
        b1.set(clicked())
        checkwhowon()
    else:
        messagebox.showinfo("Error","This button has been selected.Please,select another empty button.")

def clicked2():
    global clicked_button,count
    if b2.get()=="":
        b2.set(clicked())
        checkwhowon()
    else:
        messagebox.showinfo("Error","This button has been selected.Please,select another empty button.")

def clicked3():
    global clicked_button,count
    if b3.get()=="":
        b3.set(clicked())
        checkwhowon()
    else:
        messagebox.showinfo("Error","This button has been selected.Please,select another empty button.")

def clicked4():
    global clicked_button,count
    if b4.get()=="":
        b4.set(clicked())
        checkwhowon()
    else:
        messagebox.showinfo("Error","This button has been selected.Please,select another empty button.")

def clicked5():
    global clicked_button,count
    if b5.get()=="":
        b5.set(clicked())
        checkwhowon()
    else:
        messagebox.showinfo("Error","This button has been selected.Please,select another empty button.")

def clicked6():
    global clicked_button,count
    if b6.get()=="":
        b6.set(clicked())
        checkwhowon()
    else:
        messagebox.showinfo("Error","This button has been selected.Please,select another empty button.")

def clicked7():
    global clicked_button,count
    if b7.get()=="":
        b7.set(clicked())
        checkwhowon()
    else:
        messagebox.showinfo("Error","This button has been selected.Please,select another empty button.")

def clicked8():
    global clicked_button,count
    if b8.get()=="":
        b8.set(clicked())
        checkwhowon()
    else:
        messagebox.showinfo("Error","This button has been selected.Please,select another empty button.")

def clicked9():
    global clicked_button,count
    if b9.get()=="":
        b9.set(clicked())
        checkwhowon()
    else:
        messagebox.showinfo("Error","This button has been selected.Please,select another empty button.")


def checkwhowon():
    global winner

    if b1.get() == "X" and b2.get() == "X" and b3.get() == "X":
        button1.config(bg="red")
        button2.config(bg="red")
        button3.config(bg="red")
        winner = True
        x_player.set(x_player.get()+1)
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X WON!")
        reset()
        reset_color()

    elif b4.get() == "X" and b5.get() == "X" and b6.get() == "X":
        button4.config(bg="red")
        button5.config(bg="red")
        button6.config(bg="red")
        winner = True
        x_player.set(x_player.get() + 1)
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X WON!")
        reset()
        reset_color()

    elif b7.get() == "X" and b8.get() == "X" and b9.get()== "X":
        button7.config(bg="red")
        button8.config(bg="red")
        button9.config(bg="red")
        winner = True
        x_player.set(x_player.get() + 1)
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X WON!")
        reset()
        reset_color()

    elif b1.get() == "X" and b4.get() == "X" and b7.get() == "X":
        button1.config(bg="red")
        button4.config(bg="red")
        button7.config(bg="red")
        winner = True
        x_player.set(x_player.get() + 1)
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X WON!")
        reset()
        reset_color()

    elif b2.get() == "X" and b5.get() == "X" and b8.get() == "X":
        button2.config(bg="red")
        button5.config(bg="red")
        button8.config(bg="red")
        winner = True
        x_player.set(x_player.get() + 1)
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X WON!")
        reset()
        reset_color()

    elif b3.get() == "X" and b6.get() == "X" and b9.get() == "X":
        button3.config(bg="red")
        button6.config(bg="red")
        button9.config(bg="red")
        winner = True
        x_player.set(x_player.get() + 1)
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X WON!")
        reset()
        reset_color()

    elif b1.get() == "X" and b5.get() == "X" and b9.get() == "X":
        button1.config(bg="red")
        button5.config(bg="red")
        button9.config(bg="red")
        winner = True
        x_player.set(x_player.get() + 1)
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X WON!")
        reset()
        reset_color()

    elif b3.get() == "X" and b5.get() == "X" and b7.get() == "X":
        button3.config(bg="red")
        button5.config(bg="red")
        button7.config(bg="red")
        winner = True
        x_player.set(x_player.get() + 1)
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X WON!")
        reset()
        reset_color()

    elif b1.get() == "O" and b2.get() == "O" and b3.get() == "O":
        button1.config(bg="red")
        button2.config(bg="red")
        button3.config(bg="red")
        winner = True
        o_player.set(o_player.get() + 1)
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O WON!")
        reset()
        reset_color()

    elif b4.get() == "O" and b5.get() == "O" and b6.get() == "O":
        button4.config(bg="red")
        button5.config(bg="red")
        button6.config(bg="red")
        winner = True
        o_player.set(o_player.get() + 1)
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O WON!")
        reset()
        reset_color()

    elif b7.get() == "O" and b8.get() == "O" and b9.get() == "O":
        button7.config(bg="red")
        button8.config(bg="red")
        button9.config(bg="red")
        winner = True
        o_player.set(o_player.get() + 1)
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O WON!")
        reset()
        reset_color()

    elif b1.get() == "O" and b4.get() == "O" and b7.get() == "O":
        button1.config(bg="red")
        button4.config(bg="red")
        button7.config(bg="red")
        winner = True
        o_player.set(o_player.get() + 1)
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O WON!")
        reset()
        reset_color()

    elif b2.get() == "O" and b5.get() == "O" and b8.get() == "O":
        button2.config(bg="red")
        button5.config(bg="red")
        button8.config(bg="red")
        winner = True
        o_player.set(o_player.get() + 1)
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O WON!")
        reset()
        reset_color()

    elif b3.get() == "O" and b6.get() == "O" and b9.get() == "O":
        button3.config(bg="red")
        button6.config(bg="red")
        button9.config(bg="red")
        winner = True
        o_player.set(o_player.get() + 1)
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O WON!")
        reset()
        reset_color()

    elif b1.get() == "O" and b5.get() == "O" and b9.get() == "O":
        button1.config(bg="red")
        button5.config(bg="red")
        button9.config(bg="red")
        winner = True
        o_player.set(o_player.get() + 1)
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O WON!")
        reset()
        reset_color()

    elif b3.get() == "O" and b5.get() == "O" and b7.get() == "O":
        button3.config(bg="red")
        button5.config(bg="red")
        button7.config(bg="red")
        winner = True
        o_player.set(o_player.get() + 1)
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O WON!")
        reset()
        reset_color()



def reset():
    b1.set("")
    b2.set("")
    b3.set("")
    b4.set("")
    b5.set("")
    b6.set("")
    b7.set("")
    b8.set("")
    b9.set("")

def reset_color():
    button1.config(bg="white")
    button2.config(bg="white")
    button3.config(bg="white")
    button4.config(bg="white")
    button5.config(bg="white")
    button6.config(bg="white")
    button7.config(bg="white")
    button8.config(bg="white")
    button9.config(bg="white")

button1 = Button(text=" ", textvariable=b1, font=("bold",20), height=2, width=5, command=clicked1)
button1.grid(row=2, column=0)
button2 = Button(text=" ", textvariable=b2, font=("bold",20), height=2, width=5, command=clicked2)
button2.grid(row=2, column=1)
button3 = Button(text=" ", textvariable=b3, font=("bold",20), height=2, width=5, command=clicked3)
button3.grid(row=2, column=2)
button4 = Button(text=" ", textvariable=b4, font=("bold",20), height=2, width=5, command=clicked4)
button4.grid(row=3, column=0)
button5 = Button(text=" ", textvariable=b5, font=("bold",20), height=2, width=5, command=clicked5)
button5.grid(row=3, column=1)
button6 = Button(text=" ", textvariable=b6, font=("bold",20), height=2, width=5, command=clicked6)
button6.grid(row=3, column=2)
button7 = Button(text=" ", textvariable=b7, font=("bold",20), height=2, width=5, command=clicked7)
button7.grid(row=4, column=0)
button8 = Button(text=" ", textvariable=b8, font=("bold",20), height=2, width=5, command=clicked8)
button8.grid(row=4, column=1)
button9 = Button(text=" ", textvariable=b9, font=("bold",20), height=2, width=5, command=clicked9)
button9.grid(row=4, column=2)
reset_button = Button(text="Reset",command=reset)
reset_button.grid(row=5,column=2,padx=10,pady=10)
window.mainloop()
