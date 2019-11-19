#!/usr/bin/env python3

from tkinter import Tk, Entry, Button, Label, Scrollbar, Listbox, Grid, StringVar, IntVar, W, E, S, N

import tkinter.filedialog
import tkinter.messagebox


def retailer_app_db():

        retailer_app = Tk()
        retailer_app.title("retailer Database")
        retailer_app.geometry('650x400')

        #! Create widgets
        store_input = StringVar()
        store_entry = Entry(retailer_app, textvariable=store_input)
        store_label = Label(retailer_app, text='Store', font=('bold', 12))

        store_entry.grid(row=0, column=1, ipady=4, ipadx=4, padx=6, pady=6)
        store_label.grid(row=0, column=0, padx=2, pady=2)

        store_address_input = StringVar()
        store_address_entry = Entry(retailer_app, textvariable=store_address_input)
        store_address_label = Label(retailer_app, text='Store Address', font=('bold', 12))

        store_address_entry.grid(row=1, column=1, ipady=4, ipadx=4, padx=6, pady=6)
        store_address_label.grid(row=1, column=0, padx=2, pady=2)

        store_id_input = IntVar()
        store_id_entry = Entry(retailer_app, textvariable=store_id_input)
        store_id_label = Label(retailer_app, text='ID', font=('bold', 12))

        store_id_entry.grid(row=2, column=1, ipady=4, ipadx=4, padx=6, pady=6)
        store_id_label.grid(row=2, column=0, padx=2, pady=2)

        city_input = StringVar()
        city_entry = Entry(retailer_app, textvariable=city_input)
        city_label = Label(retailer_app, text='City', font=('bold', 12))

        city_entry.grid(row=0, column=3, ipady=4, ipadx=4, padx=6, pady=6)
        city_label.grid(row=0, column=2, padx=2, pady=2)

        postal_code_input = StringVar()
        postal_code_entry = Entry(retailer_app, textvariable=postal_code_input)
        postal_code_label = Label(retailer_app, text='Postal Code', font=('bold', 12))

        postal_code_entry.grid(row=1, column=3, ipady=4, ipadx=4, padx=6, pady=6)
        postal_code_label.grid(row=1, column=2, padx=2, pady=2)

        employer_input = StringVar()
        employer_entry = Entry(retailer_app, textvariable=employer_input)
        employer_label = Label(retailer_app, text='Employer', font=('bold', 12))

        employer_entry.grid(row=2, column=3, ipady=4, ipadx=4, padx=6, pady=6)
        employer_label.grid(row=2, column=2, padx=2, pady=2)

        #! Listboxes
        store_info = Listbox(retailer_app, height=10, width=82)
        store_info.grid(row=5, column=0, columnspan=4, ipady=4, ipadx=4, padx=6, pady=6)

        retailer_app.mainloop()

