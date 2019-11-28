#!/usr/bin/env python3

import tkinter.filedialog
import tkinter.messagebox

from tkinter import Tk, Entry, Button, Label, Scrollbar, Listbox, Grid, StringVar, W, E, S, N, font
from client_app import client_app_db
from retailer_app import retailer_app_db


#! Create window
main_menu=Tk()
main_menu.geometry('302x166')
main_menu.title('Menu')


app_font = font.Font(family='Arial',size=11,weight='bold')

#! User options
btn_client_db = Button(main_menu, text='Client Database', font=app_font, command=client_app_db)
btn_client_db.grid(row=0, column=0, ipady=2, padx=5, pady=2, sticky=W+E)

btn_retail_db = Button(main_menu, text='Retailer Database', font=app_font, command=retailer_app_db)
btn_retail_db.grid(row=1, column=0, ipady=2, padx=5, pady=4, sticky=W+E)

btn_main_db = Button(main_menu, text='Main Database', font=app_font)
btn_main_db.grid(row=2, column=0, ipady=2, padx=5, pady=4, sticky=W+E)

btn_graph = Button(main_menu, text='Graphs', font=app_font)
btn_graph.grid(row=0, column=1, ipady=2, padx=5, pady=4, sticky=W+E)

btn_search = Button(main_menu, text='Search', font=app_font)
btn_search.grid(row=1, column=1, ipady=2, padx=5, pady=4, sticky=W+E)

btn_calendar = Button(main_menu, text='Calendar', font=app_font)
btn_calendar.grid(row=2, column=1, ipady=2, padx=5, pady=4, sticky=W+E)

btn_exit = Button(main_menu, text='Exit', font=app_font)
btn_exit.grid(row=3, column=0, ipady=2, padx=5, pady=4, columnspan=2, sticky=W+E)

main_menu.mainloop()






