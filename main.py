from tkinter import *
import os
import sys
import json


padx = 4
pady = 4

ico1 = 'ico_files.png'
ico2 = 'ico_people.png'

ico1 = PhotoImage(file=ico1)
ico2 = PhotoImage(file=ico2)

#Окно выбора базы данных
window1 = Tk()

window1.title('Базы данных')
window1.geometry('300x450')
window1.resizable(FALSE, FALSE)


window1.iconphoto(True, ico1)


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


#окно выбора персоны из базы данных
window2 = Tk()


window1.iconphoto(True, ico1)

window2.title('База данных')
window2.geometry('420x490')
window2.resizable(FALSE, FALSE)

label_frame_baze_search = LabelFrame(window2, text='Поиск')
label_frame_baze_search.pack()

search_base_entry = Entry(label_frame_baze_search, width=35)
search_base_entry.grid(padx=padx, pady=pady, row=0, column=0)

search_baze_button = Button(label_frame_baze_search, text='Поиск')
search_baze_button.grid(padx=padx, pady=pady, row=0, column=1)



lisbox_bazes = Listbox(window2, width=45, height=16)
lisbox_bazes.pack(padx=padx, pady=pady)



labelbelframe_actions_bazes = LabelFrame(window2, text='Действия')
labelbelframe_actions_bazes.pack(padx=padx, pady=pady)

buttn_close = Button(labelbelframe_actions_bazes, text='Закрыть')
buttn_close.grid(padx=padx, pady=pady, row=0, column=0)

buttn_delete = Button(labelbelframe_actions_bazes, text='Удалить пункт')
buttn_delete.grid(padx=padx, pady=pady, row=0, column=1)

buttn_open = Button(labelbelframe_actions_bazes, text='Открыть')
buttn_open.grid(padx=padx, pady=pady, row=0, column=2)


#окно переименования
window_rename = Tk()


window_rename.iconphoto(True, ico1)
window_rename.title('Переименовать')
window_rename.geometry('300x100')
window_rename.resizable(FALSE, FALSE)


label_name_baze = Label(window_rename, text=f'Переименовать выбранный файл')
label_name_baze.pack(padx=padx, pady=pady)

entry_new_name = Entry(window_rename)
entry_new_name.pack(padx=padx, pady=pady)

button_set = Button(window_rename, text='Переименовать')
button_set.pack(padx=padx, pady=pady)


#окно создания базы данных
window_create_baze = Tk()


window_create_baze.iconphoto(True, ico1)
window_create_baze.title('Переименовать')
window_create_baze.geometry('300x150')
window_create_baze.resizable(FALSE, FALSE)


label_create_baze = Label(window_create_baze, text='Создать базу данных\n\nВведите название')
label_create_baze.pack(padx=padx, pady=pady)

entry_name_baze = Entry(window_create_baze)
entry_name_baze.pack(padx=padx, pady=pady)

button_set_name = Button(window_create_baze, text='Создать')
button_set_name.pack(padx=padx, pady=pady)










#defs
##вызываем окно 1 базы данных
def win1():

    window1.mainloop()

##переносим список баз данных из папки "bases"
def insert_listbox_baze():
    direct = 'main\\bases'
    list_bazes = os.listdir(direct)
    listbox_bazes.insert(END, *list_bazes)

win1()




