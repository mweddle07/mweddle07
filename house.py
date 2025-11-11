import tkinter
class MyHouse:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.main_window, width=400, height=600)
        #create square for house:
        self.canvas.create_rectangle(60,60,200,200, fill='rosy brown')
        #create square for door:
        self.canvas.create_rectangle(100,200,70,110, fill='black')
        #create windows:
        self.canvas.create_rectangle(180,180,120,90, fill='AntiqueWhite3')
        #create window decor:
        self.canvas.create_oval(100,200,70,110, fill='AntiqueWhite3')
        self.canvas.create_oval(90,160,100,150, fill='black')
        #create triangle for roof:
        self.canvas.create_line(60,60,200,40,200,40,200,60, fill='black')
        self.canvas.pack()
        tkinter.mainloop()
myhouse = MyHouse()