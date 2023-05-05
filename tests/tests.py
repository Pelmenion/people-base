from tkinter import *
import os

root = Tk()

padx = 4
pady = 4

ico1 = 'tk_ico_files.png'
ico2 = 'tk_ico_people.png'


icon_image1 = PhotoImage(file=ico1)
root.iconphoto(True, icon_image1)
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