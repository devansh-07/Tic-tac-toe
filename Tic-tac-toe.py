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
import time, threading


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
        fr_list = [f1, f2, f3, f4, f5, f6, f7, f8, f9]
        rf = random.choice(fr_list)

        if choices[fr_list.index(rf)] is None:
            for wid in rf.winfo_children():
                wid.destroy()
            break
    ch = fr_list.index(rf)+1
    put_label("X", rf, ch=ch)

    choices[ch - 1] = "X"


# To reset layout

def reset_layout(*args):
    v = options.index(var.get())

    global choices, win
    choices = [None for _ in range(9)]  # Setting the values of choices to None
    win = False

    outer_frms = [f1, f2, f3, f4, f5, f6, f7, f8, f9]

    fr_list = [[widget for widget in frm.winfo_children()] for frm in outer_frms]

    for f in fr_list:
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

    m_root = tk.Tk()
    m_root.geometry(f"180x70+{x+60}+{y+170}")
    m_root.resizable(0, 0)
    m_root.overrideredirect(True)
    m_root.configure(bg="black")

    f = tk.Frame(m_root, bg="cyan")
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
    m_root.after(1500, m_root.destroy)
    m_root.mainloop(1)


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

fr_btns1 = tk.Frame(root, padx=6, pady=10, bg="#420c09")
fr_btns1.grid(row=0, pady=0)

tk.Label(fr_btns1, text="Play against : ", fg="white", bg="#420c09").pack(padx=(34, 0), side="left")

options = ["A Friend", "Computer"]
var = tk.StringVar(root)
var.set(options[1])
var.trace('w', reset_layout)

op_menu = tk.OptionMenu(fr_btns1, var, *options)
op_menu.configure(width=10, pady=3, borderwidth=1)
op_menu.pack(padx=(0, 34), side="left")


# Outer frame for buttons

f_r = tk.Frame(root, padx=5, pady=0, bg="#111111")
f_r.grid(row=1, pady=5)


# Three inner frames

f_r0 = tk.Frame(f_r, padx=0, pady=0, bg="#2d2d2d")
f_r0.grid(row=1)

f_r1 = tk.Frame(f_r, padx=0, pady=0, bg="#03556c")
f_r1.grid(row=2)

f_r2 = tk.Frame(f_r, padx=0, pady=0, bg="#2d2d2d")
f_r2.grid(row=3)


# Three innermost frames on each inner frame

f1 = tk.Frame(f_r0, padx=25, pady=15, bg="#2d2d2d")
f1.grid(column=0, row=0)

f2 = tk.Frame(f_r0, padx=25, pady=15, bg="#03556c")
f2.grid(column=1, row=0)

f3 = tk.Frame(f_r0, padx=25, pady=15, bg="#2d2d2d")
f3.grid(column=2, row=0)

f4 = tk.Frame(f_r1, padx=25, pady=15, bg="#03556c")
f4.grid(column=0, row=1)

f5 = tk.Frame(f_r1, padx=25, pady=15, bg="#2d2d2d")
f5.grid(column=1, row=1)

f6 = tk.Frame(f_r1, padx=25, pady=15, bg="#03556c")
f6.grid(column=2, row=1)

f7 = tk.Frame(f_r2, padx=25, pady=15, bg="#2d2d2d")
f7.grid(column=0, row=2)

f8 = tk.Frame(f_r2, padx=25, pady=15, bg="#03556c")
f8.grid(column=1, row=2)

f9 = tk.Frame(f_r2, padx=25, pady=15, bg="#2d2d2d")
f9.grid(column=2, row=2)


# Second frame for buttons

fr_btns2 = tk.Frame(root, padx=10, pady=10, bg="#420c09")
fr_btns2.grid(row=4, pady=0)

reset_btn = tk.Button(fr_btns2, text="Restart", pady=3, padx=15, command=reset_layout)
reset_btn.pack(side="left", pady=0, padx=(25, 43))

quit_btn = tk.Button(fr_btns2, text="Quit", pady=3, padx=15, command=root.destroy)
quit_btn.pack(side="right", pady=0, padx=(43, 25))


# To create a layout for playing against friend

def create_lyt_against_frnd():
    global f1, f2, f3, f4, f5, f6, f7, f8, f9

    b1o = tk.Button(f1, text="O", padx=5, command=lambda: put_label("O", f1, b1o, b1x, 1))
    b1o.pack(side="right", pady=20)
    b1x = tk.Button(f1, text="X", padx=5, command=lambda: put_label("X", f1, b1o, b1x, 1))
    b1x.pack(pady=20)

    b2o = tk.Button(f2, text="O", padx=5, command=lambda: put_label("O", f2, b2o, b2x, 2))
    b2o.pack(side="right", pady=20)
    b2x = tk.Button(f2, text="X", padx=5, command=lambda: put_label("X", f2, b2o, b2x, 2))
    b2x.pack(pady=20)

    b3o = tk.Button(f3, text="O", padx=5, command=lambda: put_label("O", f3, b3o, b3x, 3))
    b3o.pack(side="right", pady=20)
    b3x = tk.Button(f3, text="X", padx=5, command=lambda: put_label("X", f3, b3o, b3x, 3))
    b3x.pack(pady=20)

    b4o = tk.Button(f4, text="O", padx=5, command=lambda: put_label("O", f4, b4o, b4x, 4))
    b4o.pack(side="right", pady=20)
    b4x = tk.Button(f4, text="X", padx=5, command=lambda: put_label("X", f4, b4o, b4x, 4))
    b4x.pack(pady=20)

    b5o = tk.Button(f5, text="O", padx=5, command=lambda: put_label("O", f5, b5o, b5x, 5))
    b5o.pack(side="right", pady=20)
    b5x = tk.Button(f5, text="X", padx=5, command=lambda: put_label("X", f5, b5o, b5x, 5))
    b5x.pack(pady=20)

    b6o = tk.Button(f6, text="O", padx=5, command=lambda: put_label("O", f6, b6o, b6x, 6))
    b6o.pack(side="right", pady=20)
    b6x = tk.Button(f6, text="X", padx=5, command=lambda: put_label("X", f6, b6o, b6x, 6))
    b6x.pack(pady=20)

    b7o = tk.Button(f7, text="O", padx=5, command=lambda: put_label("O", f7, b7o, b7x, 7))
    b7o.pack(side="right", pady=20)
    b7x = tk.Button(f7, text="X", padx=5, command=lambda: put_label("X", f7, b7o, b7x, 7))
    b7x.pack(pady=20)

    b8o = tk.Button(f8, text="O", padx=5, command=lambda: put_label("O", f8, b8o, b8x, 8))
    b8o.pack(side="right", pady=20)
    b8x = tk.Button(f8, text="X", padx=5, command=lambda: put_label("X", f8, b8o, b8x, 8))
    b8x.pack(pady=20)

    b9o = tk.Button(f9, text="O", padx=5, command=lambda: put_label("O", f9, b9o, b9x, 9))
    b9o.pack(side="right", pady=20)
    b9x = tk.Button(f9, text="X", padx=5, command=lambda: put_label("X", f9, b9o, b9x, 9))
    b9x.pack(pady=20)


# To create a layout for playing against computer

def create_lyt_against_comp():
    global f1, f2, f3, f4, f5, f6, f7, f8, f9

    b1o = tk.Button(f1, text="O", padx=5, command=lambda: put_label("O", f1, b1o, ch=1, plyr='comp'))
    b1o.pack(side="right", padx=12, pady=20)

    b2o = tk.Button(f2, text="O", padx=5, command=lambda: put_label("O", f2, b2o, ch=2, plyr='comp'))
    b2o.pack(side="right", padx=12, pady=20)

    b3o = tk.Button(f3, text="O", padx=5, command=lambda: put_label("O", f3, b3o, ch=3, plyr='comp'))
    b3o.pack(side="right", padx=12, pady=20)

    b4o = tk.Button(f4, text="O", padx=5, command=lambda: put_label("O", f4, b4o, ch=4, plyr='comp'))
    b4o.pack(side="right", padx=12, pady=20)

    b5o = tk.Button(f5, text="O", padx=5, command=lambda: put_label("O", f5, b5o, ch=5, plyr='comp'))
    b5o.pack(side="right", padx=12, pady=20)

    b6o = tk.Button(f6, text="O", padx=5, command=lambda: put_label("O", f6, b6o, ch=6, plyr='comp'))
    b6o.pack(side="right", padx=12, pady=20)

    b7o = tk.Button(f7, text="O", padx=5, command=lambda: put_label("O", f7, b7o, ch=7, plyr='comp'))
    b7o.pack(side="right", padx=12, pady=20)

    b8o = tk.Button(f8, text="O", padx=5, command=lambda: put_label("O", f8, b8o, ch=8, plyr='comp'))
    b8o.pack(side="right", padx=12, pady=20)

    b9o = tk.Button(f9, text="O", padx=5, command=lambda: put_label("O", f9, b9o, ch=9, plyr='comp'))
    b9o.pack(side="right", padx=12, pady=20)


create_lyt_against_comp()

root.mainloop()
