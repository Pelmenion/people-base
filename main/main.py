from tkinter import *
import os
import sys
import json

padx = 4
pady = 4

ico1 = 'tk_ico_files.png'
ico2 = 'tk_ico_people.png'

window1 = Tk()

window1.title('Базы данных')
window1.geometry('300x450')
window1.resizable(FALSE, FALSE)

icon_image1 = PhotoImage(file=ico1)
window1.iconphoto(True, icon_image1)


label_frame_search = LabelFrame(window1, text='Поиск')
label_frame_search.pack(padx=padx, pady=pady)

entry_search = Entry(label_frame_search, width=25)
entry_search.grid(padx=padx, pady=pady, row=0, column=0)

button_search = Button(label_frame_search, text='Поиск', height=1)
button_search.grid(padx=padx, pady=pady, row=0, column=1)


label_frame_bazes = LabelFrame(window1, text='Базы')
label_frame_bazes.pack(padx=padx, pady=pady)

listbox_bazes = Listbox(label_frame_bazes, height=8, width=33)
listbox_bazes.pack(padx=padx, pady=pady)


label_frame_action = LabelFrame(window1, text="Дейстивия")
label_frame_action.pack(padx=padx, pady=pady)

button_import = Button(label_frame_action, text='Импортировать')
button_import.grid(padx=padx, pady=pady, row=1, column=0)

button_export = Button(label_frame_action, text='Экспортировать')
button_export.grid(padx=padx, pady=pady, row=1, column=1)

button_open = Button(label_frame_action, text='Открыть')
button_open.grid(padx=padx, pady=pady, row=0, column=2)

button_delete = Button(label_frame_action, text='Удалить')
button_delete.grid(padx=padx, pady=pady, row=0, column=0)

button_edit_name = Button(label_frame_action, text='Переименовать')
button_edit_name.grid(padx=padx, pady=pady, row=0, column=0)



















#defs
def win1():
    window1.mainloop()

def insert_listbox_baze():
    direct = 'main\\bases'
    list_bazes = os.listdir(direct)
    listbox_bazes.insert(END, *list_bazes)
insert_listbox_baze()
win1()


