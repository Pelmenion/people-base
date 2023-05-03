from tkinter import *
import os

root = Tk()

padx = 4
pady = 4

ico1 = 'tk_ico_files.png'
ico2 = 'tk_ico_people.png'

icon_image1 = PhotoImage(file=ico2)
root.iconphoto(True, icon_image1)
root.title('База данных')
root.geometry('420x490')
root.resizable(FALSE, FALSE)

label_frame_baze_search = LabelFrame(root, text='Поиск')
label_frame_baze_search.pack()

search_base_entry = Entry(label_frame_baze_search, width=35)
search_base_entry.grid(padx=padx, pady=pady, row=0, column=0)

search_baze_button = Button(label_frame_baze_search, text='Поиск')
search_baze_button.grid(padx=padx, pady=pady, row=0, column=1)



lisbox_bazes = Listbox(root, width=40, height=16)
lisbox_bazes.pack(padx=padx, pady=pady)



labelbelframe_actions_bazes = LabelFrame(root, text='Действия')
labelbelframe_actions_bazes.pack(padx=padx, pady=pady)

buttn_close = Button(labelbelframe_actions_bazes, text='Закрыть')
buttn_close.grid(padx=padx, pady=pady, row=0, column=0)

buttn_delete = Button(labelbelframe_actions_bazes, text='Удалить пункт')
buttn_delete.grid(padx=padx, pady=pady, row=0, column=1)

buttn_open = Button(labelbelframe_actions_bazes, text='Открыть')
buttn_open.grid(padx=padx, pady=pady, row=0, column=2)









root.mainloop()