#!/usr/bin/env python3

import sqlite3

class client_database():

    def __init__(self, client_data):
        self.connection = sqlite3.connect(client_data)
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS client_database (client_id INTEGER PRIMARY KEY, client text, client_address text, city text, zip_code int, employer_id int, store_id int)")
        self.cursor.execute("UPDATE client_database")
        self.connection.commit()
    
    def fetch(self):
        self.cur.execute("SELECT * FROM client_database")
        rows = self.cur.fetchall()

        return rows
    
    def save(self, client, client_address, city, zip_code, employer_id, store_id):
        self.cur.execute("INSERT INTO client_database VALUES (NULL, ?, ?, ?, ?, ?, ?)", (client, client_address, city, zip_code, employer_id, store_id))
        self.connection.commit()
    
    def remove(self, id):
        self.cur.execute("DELETE FROM client_database WHERE id=?", (id,))
        self.connection.commit()

    def update(self, client, client_address, city, zip_code, employer_id, store_id):
        self.cur.execute("UPDATE client_database SET client_database = ?, client = ?, client_address = ?, city = ?, zip_code = ?, employer_id = ?, store_id = ? WHERE id = ?", (client, client_address, city, zip_code, employer_id, store_id, id))
        self.connection.commit()

    def __del__(self):
        self.connection.close()