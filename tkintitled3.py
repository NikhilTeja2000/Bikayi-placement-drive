# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 02:35:44 2022

@author: chnt2


"""
from tkinter import *

import tkinter as tk
import pandas as pd
    #from tkinter import *
import tkinter.ttk as ttk

from itertools import zip_longest
import csv
window=Tk()

def first():
        
    root = Tk()
    root.title("The Total list:")
    width = 500
    height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)
    TableMargin = Frame(root, width=500)
    TableMargin.pack(side=TOP)
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=('YEAR','CATEGORY','NAME','ID'), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('YEAR', text='YEAR', anchor=W)
    tree.heading('CATEGORY', text='CATEGORY', anchor=W)
    tree.heading('NAME', text='NAME', anchor=W)
    
    tree.heading('ID', text='ID', anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=200)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=300)
    tree.pack()
    with open('hope20.csv') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            YEAR = row['year']
            CATEGORY= row['category']
            NAME = row['name']
            
            ID= row['id']
            tree.insert("", 0, values=(YEAR,CATEGORY,NAME,ID))
    if __name__ == '__main__':
        root.mainloop()
file_frame = tk.LabelFrame(window, text="prizes by category and year")
file_frame.place(height=60, width=410, x=80, y=50)

btn=Button(file_frame, text="prize winners",command=first,width=25, fg='blue')
btn.place(x=70, y=10)
lbl=Label(window, text="List of all people who got prizes", fg='red', font=("Helvetica", 16))
lbl.place(x=70, y=10)


def ok():
    prin=variable.get()
    sub=iable.get()
        
    
    # create dataframe from csv
    studentDf = pd.read_csv("hope20.csv")
    #print(studentDf)
    
    entDict = studentDf.to_dict('list')
    
    o=list(entDict.values())
    #print(o)
    data =[o[0],o[1],o[2],o[3],o[4]]
    export_data = zip_longest(*data, fillvalue = '')
    yt=list(export_data)
    vbg=[]
    print(type(prin),type(sub))
    for rtf in yt:
        if int(prin) in rtf and sub in rtf:
            fvg=list(rtf)
            vbg.append(fvg[:3])
    print(vbg)
    root = Tk()
    root.title("Sorted data after selecting the check boxes")
    width = 500
    height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)
    TableMargin = Frame(root, width=500)
    TableMargin.pack(side=TOP)
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("Firstname", "Lastname", "Address"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('Firstname', text="Year", anchor=W)
    tree.heading('Lastname', text="Category", anchor=W)
    tree.heading('Address', text="ID", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=200)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=300)
    tree.pack()
    
    for row in vbg:
        tree.insert("", 0, values=(row[0], row[1],row[2]))
    
    if __name__ == '__main__':
        root.mainloop()


def fino():
        
    
    root = Tk()
    root.title("THE TOP 4 People are listed below")
    width = 500
    height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)
    TableMargin = Frame(root, width=500)
    TableMargin.pack(side=TOP)
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("Firstname", "Lastname", "Address"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('Firstname', text="Firstname", anchor=W)
    tree.heading('Lastname', text="Lastname", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=200)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=300)
    tree.pack()
    vbg=["Frederick Sanger", "Linus Pauling", "John Bardeen", "Marie Curie."]
    for row in vbg:
        tree.insert("", 0, values=(row))
    
    if __name__ == '__main__':
        root.mainloop()

lbl=Label(window, text="To get the prizes by category and year click below drop down boxs and click submit button", fg='red', font=("Helvetica", 16))
lbl.place(x=70, y=140)            
file_frame = tk.LabelFrame(window, text="Prizes by category and year")
file_frame.place(height=120, width=410, x=80, y=170)


OPTIONS = [1900, 1901, 1902, 1903, 1904, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1916, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1926, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1938, 1939, 1940, 1941, 1942, 1943, 1944, 1945, 1946, 1947, 1948, 1949, 1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]

variable = StringVar(window)
variable.set(OPTIONS[0])

w = OptionMenu(file_frame, variable, *OPTIONS)
w.pack()

OPTIONS = ["chemistry","economics","literature","peace","peace","physics"]

iable = StringVar(window)
iable.set(OPTIONS[0])


w = OptionMenu(file_frame, iable, *OPTIONS)
w.pack()

# Buttons
button1 = tk.Button(file_frame, text="Search",command=ok, fg='red')
button1.place(rely=0.65, relx=0.75)

file_frame = tk.LabelFrame(window, text="noble prize winners")
file_frame.place(height=70, width=410, x=80, y=370)

lbl=Label(window, text="List of all people who got  noble prizes", fg='red', font=("Helvetica", 16))
lbl.place(x=70, y=310)
btn=Button(window, text="Top 4", fg='green',command=fino)
btn.place(x=250, y=400)
window.title('Bikayi Assignment-Frontend')
window.geometry("1000x500+10+10")
window.mainloop()