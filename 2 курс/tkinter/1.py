import tkinter

class MyGUI:
    def __init__(self):
        # Создать элемент интерфейса главного окна.
        self.main_window = tkinter.Tk()
        self.bottom_frame = tkinter.Frame()

      

        
        
        self.calc_button = tkinter.Button(self.bottom_frame,
                                          text='Показать инфо',
                                          command=self.get_info)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Выйти',
                                command=self.main_window.destroy)


        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

      

   
        self.bottom_frame.pack()
        # Войти в главный цикл tkinter.
        tkinter.mainloop()

    def get_info(self):
           self.label1 = tkinter.Label(self.main_window,
                                    text='Стивен Маркус')
           self.label2 = tkinter.Label(self.main_window,
                                    text='274 Бейли')
           self.label3 = tkinter.Label(self.main_window,
                                        text='УэнзвилльБ Северная Каролина 27999')

        # Упаковать надписи, расположенные в верхней рамке.
        # Применить аргумент side='top', чтобы их
        # расположить один под другим.
           self.label1.pack(side='top')
           self.label2.pack(side='top')
           self.label3.pack(side='top')
    

# Создать экземпляр класса MyGUI.
my_gui = MyGUI()
