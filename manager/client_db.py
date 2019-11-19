#!/usr/bin/env python3

import sqlite3

class client_database():

    def __init__(self, client_data):
        self.connection = sqlite3.connect(client_data)
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS client_database (client_id INTEGER PRIMARY KEY, store text, store_address text, store_id int, city text, zip_code int, employer text)")
        self.connection.commit()