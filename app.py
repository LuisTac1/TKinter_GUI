"""
GUI with TKinter
"""

import tkinter as tk
from tkinter import *
from tkinter import ttk

root = tk.Tk()
root.title('Tkinter GUI')
root.resizable(False, False)
root.geometry('900x600+50+50')
root.config(bg='gray10')

# Frame main
main_frame = tk.Frame(root, bg='gray30')
main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.place(x=5, y=0)
main_frame.configure(width=890, height=600)

# Label root
Label_root= tk.Label(root, bg='gray10', text='This is my first GUI in Python', font=('Bold', 15), fg='gray50')
Label_root.pack(side=tk.BOTTOM)
Label_root.configure(width=200, height=1)


def menubar():
    menubar = Menu(root, )

    home = Menu(menubar, tearoff = 0, background='white', foreground='gray20', 
               activebackground='red', activeforeground='gray20')
    menubar.add_cascade(label ='Home', menu=home)
    home.add_command(label="ITEM")
    home.add_command(label="ITEM")
    home.add_command(label="ITEM")

    share = Menu(menubar, tearoff = 0, background='white', foreground='gray20', 
               activebackground='red', activeforeground='gray20')
    menubar.add_cascade(label ='Share', menu=share)
    share.add_command(label="ITEM")
    share.add_command(label="ITEM")
    share.add_command(label="ITEM")

    view = Menu(menubar, tearoff = 0,  background='white', foreground='gray20', 
               activebackground='red', activeforeground='gray20') 
    menubar.add_cascade(label ='View', menu=view)
    root.config(menu = menubar)
    view.add_command(label="ITEM")
    view.add_command(label="ITEM")
    view.add_command(label="ITEM")

menubar()


# function Top colum
def top_colum():
    # Frame top
    top_frame = tk.Frame(main_frame, bg='gray20')
    top_frame.pack(side=tk.TOP)
    top_frame.place(x=0, y=0)
    top_frame.configure(width=900, height=80)

top_colum()

def bottom_colum():
    # Frame bottom
    bottom_frame = tk.Frame(main_frame, bg='gray20')
    bottom_frame.pack(side=tk.BOTTOM)
    bottom_frame.configure(width=900, height=60)


bottom_colum()


# function right colum
def right_colum():
    # Frame right
    right_frame = tk.Frame(main_frame, bg='gray20')
    right_frame.pack(side=tk.RIGHT)
    right_frame.configure(width=125, height=600)

    # Label 1
    label_1 = tk.Label(right_frame, bg='gray25', text='item buttons')
    label_1.place(x=0, y=8)
    label_1.configure(width=18, height=1)

    # Label 2
    label_2 = tk.Label(right_frame, bg='gray25', text='item')
    label_2.place(x=0, y=200)
    label_2.configure(width=18, height=1)

    # Label 3
    label_3 = tk.Label(right_frame, bg='gray25', text='listbox')
    label_3.place(x=0, y=400)
    label_3.configure(width=18, height=1)

        # button 1
    item_button = tk.Button(right_frame, text="Item 1", bg='gray70', font=('Bold', 12), bd=1, fg='gray20',)
    item_button.place(x=1, y=30)
    item_button.configure(width=13, height=1)

    # button 2
    item_button2 = tk.Button(right_frame, text="Item 2", bg='gray70', font=('Bold', 12), bd=1, fg='gray20',)
    item_button2.place(x=1, y=60)
    item_button2.configure(width=13, height=1)

    # button 3
    item_button3 = tk.Button(right_frame, text="Item 3", bg='gray70', font=('Bold', 12), bd=1, fg='gray20',)
    item_button3.place(x=1, y=90)
    item_button3.configure(width=13, height=1)

    listbox = Listbox(right_frame, bg='gray25', bd=0)  
    listbox.insert(1,"Option 1",)  
    listbox.insert(2, "Option 2")  
    listbox.insert(3, "Option 3")  
    listbox.insert(4, "Option 4")
    listbox.insert(5, "Option 5")
    listbox.place(x=0, y=420)

right_colum()


# Button open left
while True:
    def open_left():
        left_button = tk.Button(main_frame, text="Options", bg='gray80', font=('Bold', 15), bd=0, fg='gray20', command=lambda: option_left())
        left_button.pack(side=tk.LEFT)
        left_button.place(x=5, y=10)
        left_button.pack_propagate(False)
        left_button.configure(width=7, height=2)

    open_left()
    break


# function left colum
def option_left():

    def home_page():
        home_frame = tk.Frame(main_frame)
        item = tk.Label(home_frame, text='HOME PAGE: \n\n Pege 1', font=('Bold', 30))
        item.pack()
        home_frame.pack(pady=20)

    def menu_page():
        menu_frame = tk.Frame(main_frame)
        item = tk.Label(menu_frame, text='MENU PAGE: \n\n Pege 2', font=('Bold', 30))
        item.pack()
        menu_frame.pack(pady=20)

    def contact_page():
        contact_frame = tk.Frame(main_frame)
        item = tk.Label(contact_frame, text='CONTACT PAGE: \n\n Pege 3', font=('Bold', 30))
        item.pack()
        contact_frame.pack(pady=20)

    def about_page():
        about_frame = tk.Frame(main_frame)
        item = tk.Label(about_frame, text='ABOUT PAGE: \n\n Pege 4', font=('Bold', 30))
        item.pack()
        about_frame.pack(pady=20)

    def delete_pages():
        for frame in main_frame.winfo_children():
            frame.destroy()

    def indicate(item, page):
        hide_indicate()
        item.config(bg='#CF5854')
        delete_pages()
        page()

    def hide_indicate():
        home_indicate.config(bg='gray80')
        menu_indicate.config(bg='gray70')
        contact_indicate.config(bg='gray70')
        about_indicate.config(bg='gray70')

    def sep():
        # Button Separator
        separator = ttk.Separator(option_frame, orient='horizontal')
        separator.pack(fill='x')

    
    # Frame left
    option_frame = tk.Frame(root, bg='gray25')
    option_frame.pack(side=tk.LEFT)
    option_frame.pack_propagate(False)
    option_frame.configure(width=150, height=600)

    # Home button
    home_button = tk.Button(option_frame, text="Home", bg='gray80', font=('Bold', 15), bd=0, fg='gray20', command=lambda: indicate(home_indicate, home_page))
    home_button.pack(side=tk.TOP)
    home_button.pack_propagate(False)
    home_button.configure(width=100, height=3)
    # home click indicator using label
    home_indicate = tk.Label(option_frame, text='', bg='gray80')
    home_indicate.place(x=10, y=25, width=3, height=40)
    sep()

    # Menu button
    menu_button = tk.Button(option_frame, text="Menu", bg='gray70', font=('Bold', 12), bd=0, fg='gray20', command=lambda: indicate(menu_indicate, menu_page))
    menu_button.place(x=0, y=83)
    menu_button.configure(width=100, height=2)
    menu_button.pack()
    # home click indicator using label
    menu_indicate = tk.Label(option_frame, text='', bg='gray70')
    menu_indicate.place(x=10, y=90, width=3, height=30)
    sep()

    # Contact button
    contact_button = tk.Button(option_frame, text="Contact", bg='gray70', font=('Bold', 12), bd=0, fg='gray20', command=lambda: indicate(contact_indicate, contact_page))
    contact_button.place(x=0, y=124)
    contact_button.configure(width=100, height=2)
    contact_button.pack()
    # home click indicator using label
    contact_indicate = tk.Label(option_frame, text='', bg='gray70')
    contact_indicate.place(x=10, y=140, width=3, height=30)
    sep()

    # About button
    about_button = tk.Button(option_frame, text="About", bg='gray70', font=('Bold', 12), bd=0, fg='gray20', command=lambda: indicate(about_indicate, about_page))
    about_button.place(x=0, y=165)
    about_button.configure(width=100, height=2)
    about_button.pack()
    # home click indicator using label
    about_indicate = tk.Label(option_frame, text='', bg='gray70',)
    about_indicate.place(x=10, y=185, width=3, height=30)

    # Exit button
    exit_button = tk.Button(option_frame, text="Exit", bg='gray80', font=('Bold', 12), bd=0, fg='gray20', command=lambda: root.destroy())
    exit_button.configure(width=100, height=2)
    exit_button.pack(side=tk.BOTTOM)
    sep()

    # Chackbox
    cb1 = tk.Checkbutton(option_frame, text="Radio 1", font=('Bold', 12), padx=35, bg='gray35')
    cb1.pack()
    cb2 = tk.Checkbutton(option_frame, text="Radio 2", font=('Bold', 12),  padx=35, bg='gray35')
    cb2.pack()
    cb3 = tk.Checkbutton(option_frame, text="Radio 3", font=('Bold', 12),  padx=35, bg='gray35')
    cb3.pack()


root.mainloop()
