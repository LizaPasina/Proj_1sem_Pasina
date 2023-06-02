# Импортируем библиотеки.(Рандом нужен для компьютера)
import random
# Импортируем ткинтер
from tkinter import *
from functools import partial
from tkinter import messagebox
from copy import deepcopy

# Определение хода игрока
hod = 0

# создаем пустое пространство
global board
board = [[" " for x in range(3)] for y in range(3)]

# Проверка победителя матча
# по правилам игры


def win(b, l):
    return ((b[0][0] == l and b[0][1] == l and b[0][2] == l) or
            (b[1][0] == l and b[1][1] == l and b[1][2] == l) or
            (b[2][0] == l and b[2][1] == l and b[2][2] == l) or
            (b[0][0] == l and b[1][0] == l and b[2][0] == l) or
            (b[0][1] == l and b[1][1] == l and b[2][1] == l) or
            (b[0][2] == l and b[1][2] == l and b[2][2] == l) or
            (b[0][0] == l and b[1][1] == l and b[2][2] == l) or
            (b[0][2] == l and b[1][1] == l and b[2][0] == l))

# Проверяем нажал ли игрок на кнопку


def free(i, j):
    return board[i][j] == " "

# Проверка на заполненность про-ва

def full():
    flag = True
    for i in board:
        if(i.count(' ') > 0):
            flag = False
            return flag

# Определение хода компьютера
def pc():
    possibl= []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ' ':
                possibl.append([i, j])
                move = []
                if possibl == []:
                    return
                else:
                    for let in ['O', 'X']:
                        for i in possibl:
                            boardcopy = deepcopy(board)
                            boardcopy[i[0]][i[1]] = let
                            if win(boardcopy, let):
                                return i
                    corner = []
                    for i in possibl:
                        if i in [[0, 0], [0, 2], [2, 0], [2, 2]]:
                            corner.append(i)
                    if len(corner) > 0:
                        move = random.randint(0, len(corner)-1)
                        return corner[move]
                    edge = []
                    for i in possibl:
                        if i in [[0, 1], [1, 0], [1, 2], [2, 1]]:
                            edge.append(i)
                    if len(edge) > 0:
                        move = random.randint(0, len(edge)-1)
                        return edge[move]

# Процесс игры

def txt_pc(i, j, gb, P1, P2):
    global hod
    if board[i][j] == ' ':
        if hod % 2 == 0:
            P1.config(state=DISABLED)
            P2.config(state=ACTIVE)
            board[i][j] = "X"
        else:
            button[i][j].config(state=ACTIVE)
            P2.config(state=DISABLED)
            P1.config(state=ACTIVE)
            board[i][j] = "O"
        hod += 1
        button[i][j].config(text=board[i][j])
    x = True
    if win(board, "X"):
        gb.destroy()
        x = False
        box = messagebox.showinfo("Победитель", "Выиграл игрок")
    elif win(board, "O"):
        gb.destroy()
        x = False
        box = messagebox.showinfo("Победитель", "Выиграл компьютер")
    elif(full()):
        gb.destroy()
        x = False
        box = messagebox.showinfo("Ничья", "Победила дружба")
    if(x):
        if hod % 2 != 0:
            move = pc()
            button[move[0]][move[1]].config(state=DISABLED)
            txt_pc(move[0], move[1], gb, P1, P2)

# Графический интерфейс

def gameboard_pc(game_board, l1, l2):
    game_board.resizable(False, False)
    global button
    button = []
    for i in range(3):
        m = 3+i
        button.append(i)
        button[i] = []
        for j in range(3):
            n = j
            button[i].append(j)
            get_t = partial(txt_pc, i, j, game_board, l1, l2)
            button[i][j] = Button(
                game_board, bd=5, command=get_t, height=4, width=8)
            button[i][j].grid(row=m, column=n)
    game_board.mainloop()

# Стилизация окна игры с ИИ

def withpc(game_board):
    game_board.destroy()
    game_board = Tk()
    game_board.title("Крестики-нолики")
    l1 = Label(game_board, text="Игрок : X", width=10, bg="#aab8c5",  activebackground="#aab8c5")
    l1.grid(row=1, column=1)
    l2 = Label(game_board, text="ИИ : O", width=10, bg="#8788a0")
    l2.grid(row=2, column=1)

    gameboard_pc(game_board, l1, l2)

# Граф. Интерфейс меню

def play():
    menu = Tk()
    menu.geometry("228x290")
    menu.resizable(False, False)
    menu.title("Крестики-нолики")
    wpc = partial(withpc, menu)

    B1 = Button(menu, text="Играть", command=wpc,
        activeforeground='#aab8c5',
        activebackground="#8788a0", bg="#aab8c5",
        fg="#545154", width=500, font='summer', bd=5)

    B2 = Button(menu, text="Выход", command=menu.quit, activeforeground='#aab8c5',
        activebackground="#8788a0", bg="#aab8c5", fg="#545154",
        width=500, font='summer', bd=5)

    B3 = Label(menu, text="Добро пожаловать!",
              activeforeground='#aab8c5',
              activebackground="#8788a0", bg="#aab8c5",
              fg="#545154", width=500, font='summer', bd=5)

    B1.place(relx=0.5, rely=0.4, anchor=CENTER)
    B2.place(relx=0.5, rely=0.6, anchor=CENTER)
    B3.place(relx=0.5, rely=0.1, anchor=CENTER)
    menu.mainloop()

# Вызываем начало игры
if __name__ == '__main__':
    play()