import _sqlite3
import newfile
import os
import sys

def create_database():
    conn = _sqlite3.connect('estacion_bomberos.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bomberos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            direccion TEXT NOT NULL,
            rango TEXT NOT NULL
        )
    ''')
