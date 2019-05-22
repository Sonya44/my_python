from tkinter import *
import json


lst = []
lst_delete = []


def add():  # Функция добавления задачи
    dictionary = {}
    if entry_task.get() != '' and entry_category.get() != '' and entry_time.get() != '':
        dictionary["task"] = entry_task.get()
        dictionary["category"] = entry_category.get()  # Обработка всяких исключений если пользователь что-то не ввел
        dictionary['time'] = entry_time.get()  # Ипользуется встроенная библиотека вывода сообщений Messagebox
        lst.append(dictionary)
        writer(lst)
    elif entry_task.get() == '' and entry_category.get() != '' and entry_time.get() != '':
        mb.showerror("Ошибка", "Вы не ввели задачу")
    elif entry_task.get() != '' and entry_category.get() == '' and entry_time.get() != '':
        mb.showerror("Ошибка", "Вы не ввели категорию")
    elif entry_task.get() != '' and entry_category.get() != '' and entry_time.get() == '':
        mb.showerror("Ошибка", "Вы не ввели время")
    elif entry_task.get() == '' and entry_category.get() == '' and entry_time.get() != '':
        mb.showerror("Ошибка", "Вы не ввели задачу и категорию")
    elif entry_task.get() != '' and entry_category.get() == '' and entry_time.get() == '':
        mb.showerror("Ошибка", "Вы не ввели категорию и время")
    elif entry_task.get() == '' and entry_category.get() != '' and entry_time.get() == '':
        mb.showerror("Ошибка", "Вы не ввели задачу и время")
    else:
        mb.showerror("Ошибка", "Вы ничего не ввели")



def show_list():  # Функция просмотра списка задач

    text_list_of_tasks.delete(1.0, END)  # удаляем содержимое
    try:
        button_ready_to_remove.place_forget()  # Размещаем кнопки и Text
        button_delete_frame2.place_forget()
        listbox_delete.grid_remove()
        text_list_of_tasks.grid()
        with open('todolist.json', 'r', encoding='cp1251') as json_file:  # считываем содержимое файла
            contents = json.load(json_file)
        for todo in contents:  # выводим построчно задачи
            text_list_of_tasks.configure(state=NORMAL)
            text_list_of_tasks.insert(1.0, "Задача: " + todo['task'] + " " + "Категория: " + todo[
                'category'] + " " + "Дата: " + todo['time'] + '\n')
          

    except:
        with open('todolist.json', 'r', encoding='cp1251') as json_file:
            contents = json.load(json_file)
        for todo in contents:
            text_list_of_tasks.configure(state=NORMAL)
            text_list_of_tasks.insert(1.0, "Задача: " + str(todo['task']) + " " + "Категория: " + str(todo[
                                                                                                          'category']) + " " + "Дата: " + str(
                todo['time']) + '\n')
          





def writer(something): #функция для записи заметок в список contents и добавления их в файл todo_list.json
    try:
        with open('todolist.json', 'r', encoding='cp1251') as json_file:
            contents = json.load(json_file)
        for i in something:
            contents.append(i)
    except Exception as ex:
        print(ex)

    try:
        with open('todolist.json', 'w', encoding='windows-1251') as file_write:
            json.dump(contents, file_write, sort_keys=False, ensure_ascii=False)
    except Exception as e:
        print(e)





root = Tk() #главное окно tkinter'a
root.title("Менеджер задач")
root.geometry('640x200')
frame1 = Frame(root, width=320, height=120, background="#2F2F2F")  # default color was #D3D3D3
frame2 = Frame(root, width=320, height=80, background="#2F2F2F")  # default color was #D3D3D3

# ФРЕЙМ ДЛЯ НОРМАЛЬНОГО РАСПОЛОЖЕНИЯ КНОПОК
frame3 = Frame(root, width=320, height=131, background="#2F2F2F")
frame4 = Frame(root, width=320, height=70, background="#2F2F2F")

frame1.place(x=0, y=0)
frame2.place(x=320, y=0)
frame3.place(x=0, y=69)
frame4.place(x=320, y=130)


text_list_of_tasks = Text(frame2, width=40, height=10)
text_list_of_tasks.grid(row=0, column=0, padx=1, pady=1)
text_list_of_tasks.configure(state=DISABLED)


label_task = Label(frame1, text='Задача: ', fg='white', bg="#2F2F2F")
label_task.grid(row=0, column=0, pady=1)

label_category = Label(frame1, text='Категория: ', fg='white', bg="#2F2F2F")
label_category.grid(row=1, column=0, pady=1)

label_time = Label(frame1, text='Время: ', fg='white', bg="#2F2F2F")
label_time.grid(row=2, column=0, pady=1)

entry_task = Entry(frame1, width=40)
entry_task.grid(row=0, column=1, padx=5, pady=1)

entry_category = Entry(frame1, width=40)
entry_category.grid(row=1, column=1)

entry_time = Entry(frame1, width=40)
entry_time.grid(row=2, column=1)

button_add = Button(frame3, text="Добавить", width=13, command=add, bg='#474747', fg='white',
                    activebackground='#BFB173', relief='raised')
button_add.place(x=50, y=25)


button_list_of_tasks = Button(frame3, text="Список задач", width=13, command=show_list, bg='#474747', fg='white',
                              activebackground='#BFB173', relief='raised')
button_list_of_tasks.place(x=180, y=25)


root.mainloop()
