from tkinter import *
from tkinter import ttk
from sqlite3 import *
from customtkinter import *
from tkinter import messagebox

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

def cerrarprin():
    app.destroy()

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

def datosingresar ():
    def cerrar():
        ventAgregar.destroy()

    ventAgregar = CTkToplevel(app)
    ventAgregar.title("Agregar Producto")
    ventAgregar.grab_set()

    def ingresar():
        nnombre = str(nombre.get())
        nprecio = precio.get()
        nstock = stock.get()
        nombre.delete(0, END)
        precio.delete(0, END)
        stock.delete(0, END)
        cr.execute('''
                        INSERT INTO elementos(nombre, precio, stock)
                        VALUES(?,?,?)''', (nnombre, nprecio, nstock))
        baseDeDatos.commit()
        messagebox.showinfo("Accion exitosa", "El producto fue agregado con exito")
        limpiar_tabla()
        ventAgregar.destroy()

    nombre = CTkEntry(ventAgregar)
    precio= CTkEntry(ventAgregar)
    stock = CTkEntry(ventAgregar)

    nom = CTkLabel(ventAgregar, text="Agregar nombre")
    prec = CTkLabel(ventAgregar, text="Agregar precio")
    sto = CTkLabel(ventAgregar, text="Agregar cantidad del producto")

    cerr = CTkButton(ventAgregar,text="Salir", command=cerrar)
    agre = CTkButton(ventAgregar, text="Agregar",command=ingresar)

    nom.grid(row=0, column=0, pady=5, padx=5)
    nombre.grid(row=0, column=1, pady=5, padx=5)
    prec.grid(row=1, column=0, pady=5, padx=5)
    precio.grid(row=1, column=1, pady=5, padx=5)
    sto.grid(row=2, column=0, pady=5, padx=5)
    stock.grid(row=2, column=1, pady=5, padx=5)
    cerr.grid(row=3, column=0, pady=5, padx=5)
    agre.grid(row=3, column=1, pady=5, padx=5)

app = Tk()
app.title("Tienda")

table = ttk.Treeview(app, columns= ("ID", "Nombre", "Precio", "Stock"), show ="headings")

table.heading("ID", text= "ID")
table.heading("Nombre", text= "Nombre")
table.heading("Precio", text= "Precio")
table.heading("Stock", text= "Stock")

for col in table ["columns"]:
    table.column(col, anchor="center", width=100)

table.grid(row=0, column=0, columnspan=3, pady=5, padx=5)

rellenarTabla(table)
table.after(10000, lambda: limpiar_tabla(table))

ingres = CTkButton(app, text="Agregar",command=datosingresar)
clos = CTkButton(app, text="Salir", command= cerrarprin)
elimin = CTkButton(app, text="Eliminar")

ingres.grid(row=9, column=0, pady=5, padx=5)
clos.grid(row=9, column=1, pady=5, padx=5)
elimin.grid(row=9, column=2, pady=5, padx=5)

#Se inicia el bucle principal
app.mainloop()




