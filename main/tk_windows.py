import os
import sys
from tkinter import *

padx = 4
pady = 4

ico1 = 'tk_ico.png'
ico2 = 'tk_ico_people.png'

ico1 = PhotoImage(file=ico1)
ico2 = PhotoImage(file=ico2)

wind1 = Tk()


wind1.iconphoto(True, ico1)


wind1.geometry('300x400')
wind1.title('Базы данных')


label_frame_search = LabelFrame(wind1, text='Поиск')
label_frame_search.pack(padx=padx, pady=pady)

entry_search = Entry(label_frame_search, width=25)
entry_search.grid(padx=padx, pady=pady, row=0, column=0)

button_search = Button(label_frame_search, text='Поиск', height=1)
button_search.grid(padx=padx, pady=pady, row=0, column=1)


label_frame_bazes = LabelFrame(wind1, text='Базы')
label_frame_bazes.pack(padx=padx, pady=pady)

listbox_bazes = Listbox(label_frame_bazes, height=8, width=33)
listbox_bazes.pack(padx=padx, pady=pady)


label_frame_action = LabelFrame(wind1, text="Дейстивия")
label_frame_action.pack(padx=padx, pady=pady)

button_import = Button(label_frame_action, text='Импортировать')
button_import.grid(padx=padx, pady=pady, row=0, column=0)

button_export = Button(label_frame_action, text='Экспортировать')
button_export.grid(padx=padx, pady=pady, row=1, column=0)

button_open = Button(label_frame_action, text='Открыть')
button_open.grid(padx=padx, pady=pady, row=0, column=1)

button_additionally = Button(label_frame_action, text='Дополнительно')
button_additionally.grid(padx=padx, pady=pady, row=1, column=1)

def window1():
    wind1.mainloop()

def insert_search_listbox(list_base):
    listbox_bazes.insert(END, *list_base)
