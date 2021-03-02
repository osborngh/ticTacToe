import tkinter as tk
from tkinter import font
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk
import random
class ticTacToe(tk.Tk):
    """
    Class Containing TicTacToe
    """
    #Constructor with some default values
    def __init__(self):
        super().__init__()
        self.title("TicTacToe")
        self.resizable(False, False)
        self.draw_board()

    #Game Board
    def draw_board(self):
        self.player = random.choice(['X', 'O'])
        self.board = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]
        for i in range(3):
            for j in range(3):
                self.board[i][j] = tk.Button(text = '', font = ('italic', 38, 'italic'),
                                             width = 5, height = 2, command = lambda r=i, c=j: self.main_gameflow(r,c))
                self.board[i][j].grid(row = i, column = j)
        self.status_label = ttk.Label(text = ("It's "+ self.player +"'s turn"), font =('normal', 22 , 'bold'))
        self.status_label.grid(row = 3, column = 1)

        self.button_1=ttk.Button(text='Restart', width = 25,command = self.refresh)
        self.button_1.grid(row=4,column=1)

    def available_spots(self):
        #Check all available spots
        h=[]
        for i in range(3):
            for j in range(3):
                if self.board[i][j]['text'] == '':
                    h.append((i,j))
        return h
                    
    def check_win(self):
        #Using logic to find if there are any matches
        for i in range(3):
            if self.board[i][0]['text'] == self.board[i][1]['text'] == self.board[i][2]['text'] != '':
                return 1
        for j in range(3):
            if self.board[0][j]['text'] == self.board[1][j]['text'] == self.board[2][j]['text'] != '':
                return 1
        if self.board[0][0]['text'] == self.board[1][1]['text'] == self.board[2][2]['text'] != '':
            return 1
        elif self.board[0][2]['text'] == self.board[1][1]['text'] == self.board[2][0]['text'] != '':
            return 1
        elif self.available_spots() == []:
            return 0
        else:
            return -1         
    def main_gameflow(self, r, c):
        if self.board[r][c]['text'] == '' and self.check_win() == -1:
            if self.player == 'O':
                self.board[r][c].config(text='O')
                if self.check_win() == -1:
                    self.player = 'X'
                    self.status_label.config(text=("It's X's turn"))
                elif self.check_win() == 1:
                        self.status_label.config(text="")
                        msgbox.showinfo(title = "Winner", message = "O wins")
                        self.button_1.focus()
                elif self.check_win() == 0:
                    msgbox.showinfo(title = "Winners", message = "Draw")
                    self.button_1.focus()
            elif self.player == 'X':
                self.board[r][c].config(text='X')
                if self.check_win() == -1:
                    self.player = 'O'
                    self.status_label.config(text=("It's O's turn"))
                elif self.check_win() == 1:
                    msgbox.showinfo(title = "Winner", message = "X wins")
                    self.button_1.focus()
                elif self.check_win() == 0:
                    msgbox.showinfo(title = "Winners", message = "Draw")
                    self.button_1.focus()
    def refresh(self):
        self.draw_board()
if __name__ == '__main__':
    ticTacToe()
