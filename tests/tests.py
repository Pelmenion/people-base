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
root.geometry('500x600')








root.mainloop()