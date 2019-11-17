#!/usr/bin/env python3

import sqlite3

class retail_database():
    
    def __init__(self, retail_data):
        self.connection = sqlite3.connect(manager_data)
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS manager_database (manager_id INTEGER PRIMARY KEY, manager text)")
        self.connection.commit()
            
            

