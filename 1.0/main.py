from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import lang.es as es
import lang.en as en

#Global

i = 0
lang = 0

#Accept Function

def accept():
    global lang
    lang_select = combobox1.get()
    if lang_select == "English":
        lang = 0
        select_lan.destroy()
        mainroot()
    elif lang_select == "Spanish":
        lang = 1
        select_lan.destroy()
        mainroot()
    

#Language Window

select_lan = Tk()
select_lan.title("Language Select")
select_lan.config(width=350, height=250)
select_lan.resizable(width=False, height=False)

combobox1 = Combobox(select_lan, state="readonly", width=20, height=20)
combobox1.place(x=115, y=65)
combobox1.set("English")
combobox1["values"] = ["English", "Spanish"]

button_accept = Button(select_lan, text="Accept", width=10, height=2, command= lambda: accept())
button_accept.place(x=140, y=120)

#Main Window

def mainroot():
    global lang

    root = Tk()
    root.resizable(width=False, height=False)
    if lang == 0:
        root.title(en.roottitle)
    elif lang == 1:
        root.title(es.roottitle)
    
    #Menu Bar

    bar = Menu(root)
    root.config(menu=bar)

    #Menu

    ##About

    about_menu = Menu(bar, tearoff=0)
    about_menu.add_separator()
    if lang == 0:
        about_menu.add_command(label=en.about_menu_label, command=lambda: about())
    elif lang == 1:
        about_menu.add_command(label=es.about_menu_label, command=lambda: about())
    about_menu.add_separator()

    bar.add_cascade(menu=about_menu, label="Info")

    exit_menu = Menu(bar, tearoff=0)
    exit_menu.add_separator()
    if lang == 0:
        exit_menu.add_command(label=en.exit_menu_label, command=lambda: exit())
    if lang == 1:
        exit_menu.add_command(label=es.exit_menu_label, command=lambda: exit())
    exit_menu.add_separator()

    if lang == 0:
        bar.add_cascade(menu=exit_menu, label=en.exit_cascade)
    if lang == 1:
        bar.add_cascade(menu=exit_menu, label=es.exit_cascade)

    #Text Entry

    tentry = Entry(root, font=("Calibri 20"))
    tentry.grid(row=0, column=0, columnspan=4, padx=50, pady=5)

    #Functions

    def exit():
        root.destroy()

    def about():
        if lang == 0:
            messagebox.showinfo(title=en.about_title, message=en.about_message)
        elif lang == 1:
            messagebox.showinfo(title=es.about_title, message=es.about_message)

    def click_button(value):
        global i
        tentry.insert(i, value)
        i += 1

    def clear():
        tentry_str = tentry.get()
        if tentry_str != "":
            tentry.delete(0, END)
            i = 0
        elif tentry_str == "":
            if lang == 0:
                messagebox.showinfo(message=en.clear_warn_message, title=en.clear_warn_title)
                i = 0
            elif lang == 1:
                messagebox.showinfo(message=es.clear_warn_message, title=es.clear_warn_title)
                i = 0

    def do_task():
        try:
            operation = tentry.get()
            result = eval(operation)
            tentry.delete(0, END)
            tentry.insert(0, result)
            i = 0
        except SyntaxError:
            if lang == 0:
                messagebox.showerror(message=en.syntax_err_message, title=en.syntax_err_title)
            elif lang == 1:
                messagebox.showerror(message=es.syntax_err_message, title=es.syntax_err_title)

    #Buttons

    button1 = Button(root, text="1", width=5, height=2, command= lambda: click_button(1))
    button2 = Button(root, text="2", width=5, height=2, command= lambda: click_button(2))
    button3 = Button(root, text="3", width=5, height=2, command= lambda: click_button(3))
    button4 = Button(root, text="4", width=5, height=2, command= lambda: click_button(4))
    button5 = Button(root, text="5", width=5, height=2, command= lambda: click_button(5))
    button6 = Button(root, text="6", width=5, height=2, command= lambda: click_button(6))
    button7 = Button(root, text="7", width=5, height=2, command= lambda: click_button(7))
    button8 = Button(root, text="8", width=5, height=2, command= lambda: click_button(8))
    button9 = Button(root, text="9", width=5, height=2, command= lambda: click_button(9))
    button0 = Button(root, text="0", width=20, height=2, command= lambda: click_button(0))

    button_clear = Button(root, text="AC", width=5, height=2, command= lambda: clear())
    button_paren = Button(root, text="(", width=5, height=2, command= lambda: click_button("("))
    button_paren_close = Button(root, text=")", width=5, height=2, command= lambda: click_button(")"))
    button_dot = Button(root, text=".", width=5, height=2, command= lambda: click_button("."))

    button_div = Button(root, text="/", width=5, height=2, command= lambda: click_button("/"))
    button_x = Button(root, text="x", width=5, height=2, command= lambda: click_button("*"))
    button_plus = Button(root, text="+", width=5, height=2, command= lambda: click_button("+"))
    button_dec = Button(root, text="-", width=5, height=2, command= lambda: click_button("-"))
    button_eq = Button(root, text="=", width=5, height=2, command= lambda: do_task())

    #Locate buttons

    button_clear.grid(row=1, column=0, padx=5, pady=5)
    button_paren.grid(row=1, column=1, padx=5, pady=5)
    button_paren_close.grid(row=1, column=2, padx=5, pady=5)
    button_div.grid(row=1, column=3, padx=5, pady=5)

    button7.grid(row=2, column=0, padx=5, pady=5)
    button8.grid(row=2, column=1, padx=5, pady=5)
    button9.grid(row=2, column=2, padx=5, pady=5)
    button_x.grid(row=2, column=3, padx=5, pady=5)

    button4.grid(row=3, column=0, padx=5, pady=5)
    button5.grid(row=3, column=1, padx=5, pady=5)
    button6.grid(row=3, column=2, padx=5, pady=5)
    button_plus.grid(row=3, column=3, padx=5, pady=5)

    button1.grid(row=4, column=0, padx=5, pady=5)
    button2.grid(row=4, column=1, padx=5, pady=5)
    button3.grid(row=4, column=2, padx=5, pady=5)
    button_dec.grid(row=4, column=3, padx=5, pady=5)

    button0.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
    button_dot.grid(row=5, column=2, padx=5, pady=5)
    button_eq.grid(row=5, column=3, padx=5, pady=5)

    #Mainloop

    root.mainloop()

#Language Mainloop

select_lan.mainloop()