#!/usr/bin/env python3
import sqlite3

class retail_database():

    def __init__(self, retail_data):
        self.connection = sqlite3.connect(retail_data)
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS retail_database (retail_id INTEGER PRIMARY KEY, brand text, brand_id int, product text, product_category int, stock int)")
        self.connection.commit()