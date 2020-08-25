from tkinter import *
from tkinter import messagebox
import COVID19Py

covid19 = COVID19Py.COVID19()

root = Tk()
root.geometry('300x400')
root.resizable(width=False, height=False)
root.title('COVID19 INFO')
root['bg'] = '#ccc'
root.iconbitmap('E:/Downloads/covid.ico')

def uzb():
    messagebox.showinfo('Uzbekistan', covid19.getLocationByCountryCode('UZ'))
def usa():
    messagebox.showinfo('USA', covid19.getLocationByCountryCode('US'))
def itl():
    messagebox.showinfo('Italy', covid19.getLocationByCountryCode('IT'))
def spa():
    messagebox.showinfo('Spain', covid19.getLocationByCountryCode('ES'))
def rus():
    messagebox.showinfo('Russia', covid19.getLocationByCountryCode('RU'))
def wrl():
    messagebox.showinfo('World', covid19.getLatest())

main = Label(text='Welcome to COVID19 INFO App', background='#ccc', font='SegoeUI 12')

uz = Button(text='Uzbekistan', font='SegoeUI 18', command=uzb)
us = Button(text='USA', font='SegoeUI 18', command=usa)
il = Button(text='Italia', font='SegoeUI 18', command=itl)
es = Button(text='Spain', font='SegoeUI 18', command=spa)
ru = Button(text='Russia', font='SegoeUI 18', command=rus)
wr = Button(text='World', font='SegoeUI 18', command=wrl)


main.place(x=10, y=10, relwidth=0.9, relheight=0.1)
uz.place(x=10, y=50, relwidth=0.94, relheight=0.1)
us.place(x=10, y=110, relwidth=0.94, relheight=0.1)
il.place(x=10, y=170, relwidth=0.94, relheight=0.1)
es.place(x=10, y=230, relwidth=0.94, relheight=0.1)
ru.place(x=10, y=290, relwidth=0.94, relheight=0.1)
wr.place(x=10, y=350, relwidth=0.94, relheight=0.1)

root.mainloop()