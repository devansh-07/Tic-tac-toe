"""
Tic Tac Toe

##  ##  ##

1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9

##  ##  ##


"""

import tkinter as tk
import random


root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("+600+400")
root.resizable(0, 0)
root.configure(bg="#111111", pady=5)

choices = [None for _ in range(9)]
win = False
winner = None


# To generate a random move from computer

def comp_rand_move():
    global choices
    while True:
        btnFrames = [btnFrame1, btnFrame2, btnFrame3, btnFrame4, btnFrame5, btnFrame6, btnFrame7, btnFrame8, btnFrame9]
        rf = random.choice(btnFrames)

        if choices[btnFrames.index(rf)] is None:
            for wid in rf.winfo_children():
                wid.destroy()
            break
    ch = btnFrames.index(rf)+1
    put_label("X", rf, ch=ch)

    choices[ch - 1] = "X"


# To reset layout

def reset_layout(*args):
    v = options.index(var.get())

    global choices, win
    choices = [None for _ in range(9)]  # Setting the values of choices to None
    win = False

    bntFrames = [btnFrame1, btnFrame2, btnFrame3, btnFrame4, btnFrame5, btnFrame6, btnFrame7, btnFrame8, btnFrame9]

    btnFrames0 = [[widget for widget in frm.winfo_children()] for frm in bntFrames]

    for f in btnFrames0:
        for wd in f:
            wd.destroy()

    if v == 0:
        create_lyt_against_frnd()
    else:
        create_lyt_against_comp()


# Making a window to Display result

def display_win(winner):
    x = root.winfo_x()
    y = root.winfo_y()

    resultWin = tk.Tk()
    resultWin.geometry(f"180x70+{x+60}+{y+170}")
    resultWin.resizable(0, 0)
    resultWin.overrideredirect(True)
    resultWin.configure(bg="black")

    f = tk.Frame(resultWin, bg="cyan")
    f.pack(padx=5, pady=5)
    font = ("calibri", 25)

    if winner == 0:
        lx = tk.Label(f, text="Draw!", font=font, padx=30, pady=10, fg="green", bg="#222222")
        lx.pack()
    else:
        v = options.index(var.get())
        if v == 0:
            lx = tk.Label(f, text=f"{winner} won!", font=font, padx=40, pady=10, fg="green", bg="#222222")
            lx.pack()
        else:
            txt = "You Won!" if winner == "O" else "You Lose!"
            tk.Label(f, text=txt, font=font, padx=40, pady=10, fg="green", bg="#222222").pack()
    resultWin.after(1500, resultWin.destroy)
    resultWin.mainloop(1)


# To store the values in a list

def apply_changes(choice, val):
    global choices
    choices[choice - 1] = val
    check_win()


def check_win():
    global choices, win, winner
    if choices[0] == choices[1] == choices[2] is not None:
        win = True
        winner = choices[0]
    elif choices[3] == choices[4] == choices[5] is not None:
        win = True
        winner = choices[3]
    elif choices[6] == choices[7] == choices[8] is not None:
        win = True
        winner = choices[6]
    elif choices[2] == choices[5] == choices[8] is not None:
        win = True
        winner = choices[2]
    elif choices[1] == choices[4] == choices[7] is not None:
        win = True
        winner = choices[1]
    elif choices[0] == choices[3] == choices[6] is not None:
        win = True
        winner = choices[0]
    elif choices[0] == choices[4] == choices[8] is not None:
        win = True
        winner = choices[0]
    elif choices[2] == choices[4] == choices[6] is not None:
        win = True
        winner = choices[2]

    if all(choices) and not win:
        display_win(0)
        reset_layout()

    if win:
        display_win(winner)
        reset_layout()


# To put given label ('O' or 'X') after pressing button

def put_label(n, frame, btn1=None, btn2=None, ch=0, plyr='human'):
    if btn1 is not None:
        btn1.destroy()
    if btn2 is not None:
        btn2.destroy()

    font = ("calibri", 30) if n == "O" else ("calibri", 30)
    padx = 9 if n == "O" else 10
    fg = "#dd3333" if n == "O" else "yellow"

    lbl = tk.Label(frame, text=n, font=font, fg=fg, bg="#2d2d2d", padx=padx, pady=10)
    lbl.pack()

    if ch in [2, 4, 6, 8]:
        lbl.configure(bg="#03556c")
    apply_changes(ch, n)

    if plyr == 'comp':
        comp_rand_move()


# First frame for buttons

topFrame = tk.Frame(root, padx=6, pady=10, bg="#420c09")
topFrame.grid(row=0, pady=0)

tk.Label(topFrame, text="Play against : ", fg="white", bg="#420c09").pack(padx=(34, 0), side="left")

options = ["A Friend", "Computer"]
var = tk.StringVar(root)
var.set(options[1])
var.trace('w', reset_layout)

optionMenu = tk.OptionMenu(topFrame, var, *options)
optionMenu.configure(width=10, pady=3, borderwidth=1)
optionMenu.pack(padx=(0, 34), side="left")


# Outer frame for buttons

outerFrame = tk.Frame(root, padx=5, pady=0, bg="#111111")
outerFrame.grid(row=1, pady=5)


# Three inner frames

innerFrame0 = tk.Frame(outerFrame, padx=0, pady=0, bg="#2d2d2d")
innerFrame0.grid(row=1)

innerFrame1 = tk.Frame(outerFrame, padx=0, pady=0, bg="#03556c")
innerFrame1.grid(row=2)

innerFrame2 = tk.Frame(outerFrame, padx=0, pady=0, bg="#2d2d2d")
innerFrame2.grid(row=3)


# Three innermost frames on each inner frame

btnFrame1 = tk.Frame(innerFrame0, padx=25, pady=15, bg="#2d2d2d")
btnFrame1.grid(column=0, row=0)

btnFrame2 = tk.Frame(innerFrame0, padx=25, pady=15, bg="#03556c")
btnFrame2.grid(column=1, row=0)

btnFrame3 = tk.Frame(innerFrame0, padx=25, pady=15, bg="#2d2d2d")
btnFrame3.grid(column=2, row=0)

btnFrame4 = tk.Frame(innerFrame1, padx=25, pady=15, bg="#03556c")
btnFrame4.grid(column=0, row=1)

btnFrame5 = tk.Frame(innerFrame1, padx=25, pady=15, bg="#2d2d2d")
btnFrame5.grid(column=1, row=1)

btnFrame6 = tk.Frame(innerFrame1, padx=25, pady=15, bg="#03556c")
btnFrame6.grid(column=2, row=1)

btnFrame7 = tk.Frame(innerFrame2, padx=25, pady=15, bg="#2d2d2d")
btnFrame7.grid(column=0, row=2)

btnFrame8 = tk.Frame(innerFrame2, padx=25, pady=15, bg="#03556c")
btnFrame8.grid(column=1, row=2)

btnFrame9 = tk.Frame(innerFrame2, padx=25, pady=15, bg="#2d2d2d")
btnFrame9.grid(column=2, row=2)


# Second frame for buttons

bottomFrame = tk.Frame(root, padx=10, pady=10, bg="#420c09")
bottomFrame.grid(row=4, pady=0)

btnReset = tk.Button(bottomFrame, text="Restart", pady=3, padx=15, command=reset_layout)
btnReset.pack(side="left", pady=0, padx=(25, 43))

btnQuit = tk.Button(bottomFrame, text="Quit", pady=3, padx=15, command=root.destroy)
btnQuit.pack(side="right", pady=0, padx=(43, 25))


# To create a layout for playing against friend

def create_lyt_against_frnd():
    global btnFrame1, btnFrame2, btnFrame3, btnFrame4, btnFrame5, btnFrame6, btnFrame7, btnFrame8, btnFrame9

    btn1o = tk.Button(btnFrame1, text="O", padx=5, command=lambda: put_label("O", btnFrame1, btn1o, btn1x, 1))
    btn1o.pack(side="right", pady=20)
    btn1x = tk.Button(btnFrame1, text="X", padx=5, command=lambda: put_label("X", btnFrame1, btn1o, btn1x, 1))
    btn1x.pack(pady=20)

    btn2o = tk.Button(btnFrame2, text="O", padx=5, command=lambda: put_label("O", btnFrame2, btn2o, btn2x, 2))
    btn2o.pack(side="right", pady=20)
    btn2x = tk.Button(btnFrame2, text="X", padx=5, command=lambda: put_label("X", btnFrame2, btn2o, btn2x, 2))
    btn2x.pack(pady=20)

    btn3o = tk.Button(btnFrame3, text="O", padx=5, command=lambda: put_label("O", btnFrame3, btn3o, btn3x, 3))
    btn3o.pack(side="right", pady=20)
    btn3x = tk.Button(btnFrame3, text="X", padx=5, command=lambda: put_label("X", btnFrame3, btn3o, btn3x, 3))
    btn3x.pack(pady=20)

    btn4o = tk.Button(btnFrame4, text="O", padx=5, command=lambda: put_label("O", btnFrame4, btn4o, btn4x, 4))
    btn4o.pack(side="right", pady=20)
    btn4x = tk.Button(btnFrame4, text="X", padx=5, command=lambda: put_label("X", btnFrame4, btn4o, btn4x, 4))
    btn4x.pack(pady=20)

    btn5o = tk.Button(btnFrame5, text="O", padx=5, command=lambda: put_label("O", btnFrame5, btn5o, btn5x, 5))
    btn5o.pack(side="right", pady=20)
    btn5x = tk.Button(btnFrame5, text="X", padx=5, command=lambda: put_label("X", btnFrame5, btn5o, btn5x, 5))
    btn5x.pack(pady=20)

    btn6o = tk.Button(btnFrame6, text="O", padx=5, command=lambda: put_label("O", btnFrame6, btn6o, btn6x, 6))
    btn6o.pack(side="right", pady=20)
    btn6x = tk.Button(btnFrame6, text="X", padx=5, command=lambda: put_label("X", btnFrame6, btn6o, btn6x, 6))
    btn6x.pack(pady=20)

    btn7o = tk.Button(btnFrame7, text="O", padx=5, command=lambda: put_label("O", btnFrame7, btn7o, btn7x, 7))
    btn7o.pack(side="right", pady=20)
    btn7x = tk.Button(btnFrame7, text="X", padx=5, command=lambda: put_label("X", btnFrame7, btn7o, btn7x, 7))
    btn7x.pack(pady=20)

    btn8o = tk.Button(btnFrame8, text="O", padx=5, command=lambda: put_label("O", btnFrame8, btn8o, btn8x, 8))
    btn8o.pack(side="right", pady=20)
    btn8x = tk.Button(btnFrame8, text="X", padx=5, command=lambda: put_label("X", btnFrame8, btn8o, btn8x, 8))
    btn8x.pack(pady=20)

    btn9o = tk.Button(btnFrame9, text="O", padx=5, command=lambda: put_label("O", btnFrame9, btn9o, btn9x, 9))
    btn9o.pack(side="right", pady=20)
    btn9x = tk.Button(btnFrame9, text="X", padx=5, command=lambda: put_label("X", btnFrame9, btn9o, btn9x, 9))
    btn9x.pack(pady=20)


# To create a layout for playing against computer

def create_lyt_against_comp():
    global btnFrame1, btnFrame2, btnFrame3, btnFrame4, btnFrame5, btnFrame6, btnFrame7, btnFrame8, btnFrame9

    btn1o = tk.Button(btnFrame1, text="O", padx=5, command=lambda: put_label("O", btnFrame1, btn1o, ch=1, plyr='comp'))
    btn1o.pack(side="right", padx=12, pady=20)

    btn2o = tk.Button(btnFrame2, text="O", padx=5, command=lambda: put_label("O", btnFrame2, btn2o, ch=2, plyr='comp'))
    btn2o.pack(side="right", padx=12, pady=20)

    btn3o = tk.Button(btnFrame3, text="O", padx=5, command=lambda: put_label("O", btnFrame3, btn3o, ch=3, plyr='comp'))
    btn3o.pack(side="right", padx=12, pady=20)

    btn4o = tk.Button(btnFrame4, text="O", padx=5, command=lambda: put_label("O", btnFrame4, btn4o, ch=4, plyr='comp'))
    btn4o.pack(side="right", padx=12, pady=20)

    btn5o = tk.Button(btnFrame5, text="O", padx=5, command=lambda: put_label("O", btnFrame5, btn5o, ch=5, plyr='comp'))
    btn5o.pack(side="right", padx=12, pady=20)

    btn6o = tk.Button(btnFrame6, text="O", padx=5, command=lambda: put_label("O", btnFrame6, btn6o, ch=6, plyr='comp'))
    btn6o.pack(side="right", padx=12, pady=20)

    btn7o = tk.Button(btnFrame7, text="O", padx=5, command=lambda: put_label("O", btnFrame7, btn7o, ch=7, plyr='comp'))
    btn7o.pack(side="right", padx=12, pady=20)

    btn8o = tk.Button(btnFrame8, text="O", padx=5, command=lambda: put_label("O", btnFrame8, btn8o, ch=8, plyr='comp'))
    btn8o.pack(side="right", padx=12, pady=20)

    btn9o = tk.Button(btnFrame9, text="O", padx=5, command=lambda: put_label("O", btnFrame9, btn9o, ch=9, plyr='comp'))
    btn9o.pack(side="right", padx=12, pady=20)


create_lyt_against_comp()

root.mainloop()
