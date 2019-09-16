import tkinter

class MyGUI:
    def __init__(self):
        # Создать элемент интерфейса главного окна.
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

      

        
        
        self.calc_button1 = tkinter.Button(self.bottom_frame,
                                          text='sinister',
                                          command=self.get_info1)
        self.calc_button2 = tkinter.Button(self.bottom_frame,
                                          text='dexter',
                                          command=self.get_info2)
        self.calc_button3 = tkinter.Button(self.bottom_frame,
                                          text='medium',
                                          command=self.get_info3)


        self.calc_button1.pack(side='left')
        self.calc_button2.pack(side='left')
        self.calc_button3.pack(side='left')
        

      
 
        self.top_frame.pack()
        self.bottom_frame.pack()
        # Войти в главный цикл tkinter.
        tkinter.mainloop()

    def get_info1(self):
           self.label1 = tkinter.Label(self.top_frame,
                                    text='левый')
        
           self.label1.pack(side='top')
    
    def get_info2(self):
           self.label2 = tkinter.Label(self.top_frame,
                                    text='правый')
        
           self.label2.pack(side='top')

    def get_info3(self):
           self.label3 = tkinter.Label(self.top_frame,
                                    text='средний')
        
           self.label3.pack(side='top')      
           
     
           
# Создать экземпляр класса MyGUI.
my_gui = MyGUI()
