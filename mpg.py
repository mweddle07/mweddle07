import tkinter
class MPG:
    def __init__(self):
        self.main_window = tkinter.Tk()
        
        self.gallons_frame = tkinter.Frame(self.main_window)        
        self.gallons_label = tkinter.Label(self.gallons_frame, 
                                           text = "How many gallons of gas does your car hold: ")
        self.gallons_entry = tkinter.Entry(self.gallons_frame, 
                                           width = 20)
        
        self.gallons_label.pack(side='left')
        self.gallons_entry.pack(side='left')
        
        self.miles_frame = tkinter.Frame(self.main_window)
        self.miles_label = tkinter.Label(self.miles_frame,
                                           text = "Number of miles your car can drive on full tank: ")
        self.miles_entry = tkinter.Entry(self.miles_frame, 
                                           width = 20) 
        
        self.miles_label.pack(side='left')
        self.miles_entry.pack(side='left')
        
        self.mpg_frame = tkinter.Frame(self.main_window)
        self.result_label = tkinter.Label(self.mpg_frame,  text='Miles Per Gallon=')
        self.mpg = tkinter.StringVar()
        self.mpg_label = tkinter.Label(self.mpg_frame, 
                                       textvariable=self.mpg)
        
        self.result_label.pack (side='left')
        self.mpg_label.pack(side = 'left')
        
        self.button_frame = tkinter.Frame(self.main_window)
        self.calc_button = tkinter.Button(self.button_frame, 
                                          text='Calculate MPG', 
                                          command=self.calc_mpg)
        
        self.calc_button.pack(side='left')

        self.gallons_frame.pack()
        self.miles_frame.pack()
        self.button_frame.pack()
        self.mpg_frame.pack()

        tkinter.mainloop()
        
    def calc_mpg(self): 
        self.gallons = float(self.gallons_entry.get())
        self.miles = float(self.miles_entry.get())

        print(self.gallons, self.miles)

        self.mpg = self.miles / self.gallons
        self.result_label['text'] = "'Miles Per Gallon = '{:0.2f}".format(self.mpg)

mpg = MPG()