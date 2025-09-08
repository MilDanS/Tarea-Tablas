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

def rellenarTabla (table):
    baseDeDatos = connect("tienda.db")
    cr = baseDeDatos.cursor()
    cr.execute('''SELECT * FROM elementos''')
    datos = cr.fetchall()
    for dato in datos:
        table.insert("", "end", values=dato)

def limpiar_tabla(table):
    for item in table.get_children():
        table.delete(item)

def ingresar():
    nnombre = nombre.get()
    nprecio = precio.get()
    nstock = stock.get()

    cr.execute('''
                    INSERT INTO elementos(nombre, precio, stock)
                    VALUES(?,?,?)''', (nnombre, nprecio, nstock))
    baseDeDatos.commit()

app = Tk()
app.title("Tienda")

table = ttk.Treeview(app, columns= ("ID", "Nombre", "Precio", "Stock"), show ="headings")

table.heading("ID", text= "ID")
table.heading("Nombre", text= "Nombre")
table.heading("Precio", text= "Precio")
table.heading("Stock", text= "Stock")

for col in table ["columns"]:
    table.column(col, anchor="center", width=100)

table.pack()

rellenarTabla(table)
table.after(10000, lambda: limpiar_tabla(table))

nombre = Entry(app)
precio = Entry(app)
stock = Entry(app)

bingresar = Button(app, text="Ingresar", command=ingresar)

nombre.pack()
precio.pack()
stock.pack()
bingresar.pack()

#Se inicia el bucle principal
app.mainloop()




