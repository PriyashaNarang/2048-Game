from tkinter import Frame,Label,CENTER
import constants
import logics
import constants as c
class Game2048(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.grid()
        self.master.title('2048')
        self.master.bind("<Key>",self.key_down)
        self.commands={c.KEY_UP:logics.up_move,c.KEY_DOWN:logics.down_move,c.KEY_LEFT:logics.left_move,
                       c.KEY_RIGHT:logics.right_move}
        self.grid_cells=[]
        self.init_grid()
        self.init_matrix()
        self.update_grid_cells()
        self.mainloop()
    def init_grid(self):
        background=Frame(self,bg=c.GAME_BACKGROUND_COLOR,width=c.SIZE,height=c.SIZE)
        background.grid()
        for i in range(c.MAT_LEN):
            grid_row=[]
            for j in range(c.MAT_LEN):
                cell=Frame(background,bg=c.EMPTY_CELL_COLOR,width=c.SIZE/c.MAT_LEN,
                           height=c.SIZE/c.MAT_LEN)
                cell.grid(row=i,column=j,padx=c.MAT_PADDING,pady=c.MAT_PADDING)
                t=Label(master=cell,text="",bg=c.EMPTY_CELL_COLOR,
                        justify=CENTER,font=c.FONT,width=5,height=2)
                t.grid()
                grid_row.append(t)
            self.grid_cells.append(grid_row)
    def init_matrix(self):
        self.matrix=logics.start_game()
        logics.add_new_two(self.matrix)
        logics.add_new_two(self.matrix)
    def update_grid_cells(self):
        for i in range(c.MAT_LEN):
            for j in range(c.MAT_LEN):
                new_no=self.matrix[i][j]
                if new_no==0:
                    self.grid_cells[i][j].configure(text="",bg=c.EMPTY_CELL_COLOR)
                else:
                    self.grid_cells[i][j].configure(text=str(new_no),bg=c.BACKGROUND_CELL_COLOR[new_no],
                                                    fg=c.BACKGROUND_TEXT_COLOR[new_no])
        self.update_idletasks()
    def key_down(self,event):
        key=repr(event.char)
        if key in self.commands:
            self.matrix,c=self.commands[repr(event.char)](self.matrix)
            if c:
                logics.add_new_two(self.matrix)
                self.update_grid_cells()
                c=False
                if logics.get_current_state(self.matrix)=="WON":
                    self.grid_cells[1][1].configure(text="YOU",bg=constants.EMPTY_CELL_COLOR)
                    self.grid_cells[1][2].configure(text="WIN!",bg=constants.EMPTY_CELL_COLOR)
                if logics.get_current_state(self.matrix)=="LOST":
                    self.grid_cells[1][1].configure(text="YOU", bg=constants.EMPTY_CELL_COLOR)
                    self.grid_cells[1][2].configure(text="LOSE!", bg=constants.EMPTY_CELL_COLOR)
g=Game2048()