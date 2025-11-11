import tkinter
class C2F:
    def __init__(self):
        self.main_window = tkinter.Tk()
        
        self.cel_frame = tkinter.Frame(self.main_window)        
        self.cel_label = tkinter.Label(self.cel_frame, 
                                           text = "Enter temperature in Celsius: ")
        self.cel_entry = tkinter.Entry(self.cel_frame, 
                                           width = 20)
        
        self.cel_label.pack(side='left')
        self.cel_entry.pack(side='left')
        
        self.fah_frame = tkinter.Frame(self.main_window)
        self.result_label = tkinter.Label(self.fah_frame,  text='Temperature in Fahrenheit=')
        self.result_label.pack (side='left')
        self.fah = tkinter.StringVar()
        self.fah_label = tkinter.Label(self.fah_frame, 
                                       textvariable=self.fah)
        
        self.button_frame = tkinter.Frame(self.main_window)
        self.convert_button = tkinter.Button(self.button_frame, 
                                          text='Convert', 
                                          command=self.calc_cel)
        
        self.convert_button.pack(side='left')

        self.cel_frame.pack()
        self.button_frame.pack()
        self.fah_frame.pack()


        tkinter.mainloop()
        
    def calc_cel(self): 
        self.cel = float(self.cel_entry.get())

        print(self.cel)
        self.fah = self.cel * 9/5 + 32
        self.result_label['text'] = "Temperature in Fahrenheit = '{0}".format(self.fah)

c2f = C2F()
