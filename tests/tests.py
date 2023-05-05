from tkinter import *
import os

root = Tk()

padx = 4
pady = 4

ico1 = 'ico_files.png'
ico2 = 'ico_people.png'

ico1 = PhotoImage(file=ico1)
ico2 = PhotoImage(file=ico2)


root.iconphoto(True, ico1)

root.title('Переименовать')
root.geometry('300x150')
root.resizable(FALSE, FALSE)


label_create_baze = Label(root, text='Создать базу данных\n\nВведите название')
label_create_baze.pack(padx=padx, pady=pady)

entry_name_baze = Entry(root)
entry_name_baze.pack(padx=padx, pady=pady)

button_set_name = Button(root, text='Создать')
button_set_name.pack(padx=padx, pady=pady)

root.mainloop()