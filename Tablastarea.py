from tkinter import *
from tkinter import ttk
from sqlite3 import *

baseDeDatos = connect("tienda.db")
cr = baseDeDatos.cursor()

def tabla():
    cr.execute('''CREATE TABLE IF NOT EXISTS elementos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL,
            stock INTEGER NOT NULL
            );''')
    baseDeDatos.commit()

def rellenarTabla (elementos):
    baseDeDatos = connect("tienda.db")
    cr = baseDeDatos.cursor()
    cr.execute('''SELECT * FROM elementos''')
    datos = cr.fetchall()
    for dato in datos:
        elementos.insert("", "end", values=dato)

def limpiar_tabla(elementos):
    for item in elementos.get_children():
        elementos.delete(item)

