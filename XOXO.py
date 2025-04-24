import tkinter as tk
from tkinter import messagebox
class XOXO:
    def __init__(self):
        self.current_player='X'
        self.board=[["","",""],["","",""],["","",""]]
        self.window=tk.Tk()
        self.window.title("TIC TOK TO")

        self.buttongrid = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.window,text="" ,width=20,height=10,command=lambda i=i,j=j: self.make_move(i,j))
                button.grid(row=i,column=j)
                row.append(button)
            self.buttongrid.append(row)

    def make_move(self,row,col):
        if self.board[row][col] == '':
            self.board[row][col] = self.current_player
            self.buttongrid[row][col].config(text=self.current_player)
            if self.current_winner(self.current_player):
                messagebox.showinfo('Game over', 'Winner is ' +self.current_player)
                self.window.quit()
            elif self.draw():
                messagebox.showinfo('Game over','Its Draw')
                self.window.quit()

            self.current_player= 'O' if self.current_player == 'X' else 'X'
                               

    def current_winner(self,player):
        for i in range(3):
            if player == self.board[i][0] == self.board[i][1] == self.board[i][2]:
                return True
            if player == self.board[0][i] == self.board[1][i] == self.board[2][i]:
                return True
        if player == self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return True
        if player == self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return True
        return False
    
    def draw(self):
        for r in self.board:
            if "" in r:
                return False
            return True 
        

    def run(self):
        self.window.mainloop()

game = XOXO()
game.run()                    


