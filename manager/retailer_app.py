#!/usr/bin/env python3

from tkinter import Tk, Entry, Button, Label, Scrollbar, Listbox, Grid, StringVar, IntVar, W, E, S, N

import tkinter.filedialog
import tkinter.messagebox


def retailer_app_db():

        retailer_app = Tk()
        retailer_app.title("retailer Database")
        retailer_app.geometry('650x400')

        #! Create widgets
        brand_input = StringVar()
        brand_entry = Entry(retailer_app, textvariable=brand_input)
        brand_label = Label(retailer_app, text='Brand', font=('bold', 12))

        brand_entry.grid(row=0, column=1, ipady=4, ipadx=4, padx=6, pady=6)
        brand_label.grid(row=0, column=0, padx=2, pady=2)

        brand_id_input = IntVar()
        brand_id_entry = Entry(retailer_app, textvariable=brand_id_input)
        brand_id_label = Label(retailer_app, text='ID', font=('bold', 12))

        brand_id_entry.grid(row=1, column=1, ipady=4, ipadx=4, padx=6, pady=6)
        brand_id_label.grid(row=1, column=0, padx=2, pady=2)

        product_input = StringVar()
        product_entry = Entry(retailer_app, textvariable=product_input)
        product_label = Label(retailer_app, text='Product', font=('bold', 12))

        product_entry.grid(row=0, column=3, ipady=4, ipadx=4, padx=6, pady=6)
        product_label.grid(row=0, column=2, padx=2, pady=2)

        Category_input = StringVar()
        Category_entry = Entry(retailer_app, textvariable=Category_input)
        Category_label = Label(retailer_app, text='Category', font=('bold', 12))

        Category_entry.grid(row=1, column=3, ipady=4, ipadx=4, padx=6, pady=6)
        Category_label.grid(row=1, column=2, padx=2, pady=2)

        stock_input = IntVar()
        stock_entry = Entry(retailer_app, textvariable=stock_input)
        stock_label = Label(retailer_app, text='Stock', font=('bold', 12))

        stock_entry.grid(row=2, column=3, ipady=4, ipadx=4, padx=6, pady=6)
        stock_label.grid(row=2, column=2, padx=2, pady=2)

        #! Listboxes
        brand_info = Listbox(retailer_app, height=10, width=82)
        brand_info.grid(row=5, column=0, columnspan=4, ipady=4, ipadx=4, padx=6, pady=6)

        retailer_app.mainloop()

