#!/usr/bin/env python3

from tkinter import Tk, Entry, Button, Label, Scrollbar, Listbox, Grid, StringVar, IntVar, W, E, S, N, font

import tkinter.filedialog
import tkinter.messagebox

import client_db


c_db = client_db('client_db')

def client_app_db():

        client_app = Tk()
        client_app.title("Client Database")
        client_app.geometry('620x465')

        app_font = font.Font(family='Arial',size=11,weight='bold')

        #!Commands
        def save(c_db):
                #saving the user data of the entries
                c_db.insert(store.get(), product_data.get(), 
                    cod_data.get(), price_data.get())



        #! Create widgets
        store_input = StringVar()
        store_entry = Entry(client_app, textvariable=store_input)
        store_label = Label(client_app, text='Store', font=app_font)

        store_entry.grid(row=0, column=1, ipady=4, ipadx=4, padx=6, pady=6)
        store_label.grid(row=0, column=0, padx=2, pady=2)

        store_address_input = StringVar()
        store_address_entry = Entry(client_app, textvariable=store_address_input)
        store_address_label = Label(client_app, text='Store Address', font=app_font)

        store_address_entry.grid(row=1, column=1, ipady=4, ipadx=4, padx=6, pady=6)
        store_address_label.grid(row=1, column=0, padx=2, pady=2)

        store_id_input = IntVar()
        store_id_entry = Entry(client_app, textvariable=store_id_input)
        store_id_label = Label(client_app, text='ID', font=app_font)

        store_id_entry.grid(row=2, column=1, ipady=4, ipadx=4, padx=6, pady=6)
        store_id_label.grid(row=2, column=0, padx=2, pady=2)

        city_input = StringVar()
        city_entry = Entry(client_app, textvariable=city_input)
        city_label = Label(client_app, text='City', font=app_font)

        city_entry.grid(row=0, column=3, ipady=4, ipadx=4, padx=6, pady=6)
        city_label.grid(row=0, column=2, padx=2, pady=2)

        postal_code_input = StringVar()
        postal_code_entry = Entry(client_app, textvariable=postal_code_input)
        postal_code_label = Label(client_app, text='Postal Code', font=app_font)

        postal_code_entry.grid(row=1, column=3, ipady=4, ipadx=4, padx=6, pady=6)
        postal_code_label.grid(row=1, column=2, padx=2, pady=2)

        employer_input = StringVar()
        employer_entry = Entry(client_app, textvariable=employer_input)
        employer_label = Label(client_app, text='Employer', font=app_font)

        employer_entry.grid(row=2, column=3, ipady=4, ipadx=4, padx=6, pady=6)
        employer_label.grid(row=2, column=2, padx=2, pady=2)

        #! Listbox
        store_info = Listbox(client_app, height=10, width=82)
        store_info.grid(row=5, column=0, columnspan=4, ipady=4, ipadx=4, padx=6, pady=6)

        client_entry_info = Listbox(client_app, height=15, width=82)
        client_entry_info.grid(row=6, column=0, columnspan=4, ipady=4, ipadx=4, padx=6, pady=6)

        #! Buttons
        btn_save = Button(client_app, text='SAVE', font=app_font)
        btn_save.grid(row=7, column=0, padx=2, pady=2)

        btn_remove = Button(client_app, text='REMOVE', font=app_font)
        btn_remove.grid(row=7, column=1, padx=2, pady=2)

        btn_clear = Button(client_app, text='CLEAR', font=app_font)
        btn_clear.grid(row=7, column=2, padx=2, pady=2)

        btn_clear = Button(client_app, text='UPDATE', font=app_font)
        btn_clear.grid(row=7, column=3, padx=2, pady=2)

        client_app.mainloop()
