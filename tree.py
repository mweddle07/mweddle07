import tkinter
import tkinter.font
class TreeAge:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.main_window, width=200, height=200)
        myfont=tkinter.font.Font(family='Helvetica', size=7)
        self.canvas.create_oval(70,70,110,110)
        self.canvas.create_text(90,87,text='1 Year', font=myfont)
        self.canvas.create_oval(55,55,125,125)
        self.canvas.create_text(90,65,text='2 Years', font=myfont)
        self.canvas.create_oval(40,40,140,140)
        self.canvas.create_text(90,50,text='3 Years', font=myfont)
        self.canvas.create_oval(25,25,155,155)
        self.canvas.create_text(90,35,text='4 Years', font=myfont)
        self.canvas.create_oval(10,10,170,170)
        self.canvas.create_text(90,20,text='5 Years', font=myfont)
        self.canvas.pack()
        tkinter.mainloop()
treeage=TreeAge()
