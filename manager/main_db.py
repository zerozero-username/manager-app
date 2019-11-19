#!/usr/bin/env python3

import sqlite3

class main_database():

    def __init__(self, main_data):
        self.connection = sqlite3.connect(main_data)
        self.cursor = self.connection.cursor()
        
        self.cursor.execute("CREATE TABLE IF NOT EXISTS main_database (main_id INTEGER PRIMARY KEY, store text, store_address text, store_id int, city text, postal_code int, employer text)")
        self.cursor.execute("UPDATE main_database, client_database, SET main_database.store_id = client_database.store_id, main_database.store = client_database.store, main_database.store_address = client_database.store_address, main_database.city = client_database.city WHERE main_database.store_id = client_database.store_id")
        self.connection.commit()
    
