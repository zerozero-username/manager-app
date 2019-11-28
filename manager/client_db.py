#!/usr/bin/env python3

import sqlite3

class client_database():

    def __init__(self, client_data):
        self.connection = sqlite3.connect(client_data)
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS client_database (client_id INTEGER PRIMARY KEY, store text, store_address text, store_id int, city text, zip_code int, employer text)")
        self.cursor.execute("UPDATE client_database")
        self.connection.commit()
    
    def fetch(self):
        self.cur.execute("SELECT * FROM client_database")
        rows = self.cur.fetchall()

        return rows
    
    def save(store, store_address, store_id, city, zip_code, employer):
        self.cur.execute("INSERT INTO client_database VALUES (NULL, ?, ?, ?, ?, ?, ?)", (store, store_address, store_id, city, zip_code, employer))
        self.connection.commit()
    
    def remove(self, id):
        self.cur.execute("DELETE FROM client_database WHERE id=?", (id,))
        self.connection.commit()

    def update(store, store_address, store_id, city, zip_code, employer):
        self.cur.execute("UPDATE client_database SET client_database = ?, store = ?, store_address = ?, city = ?, zip_code = ?, employer = ? WHERE id = ?", (store, store_address, store_id, city, zip_code, employer, id))
        self.connection.commit()

    def __del__(self):
        self.connection.close()