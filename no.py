nnombre = nombre.get()
        nprecio = precio.get()
        nstock = stock.get()

        cr.execute('''
                        INSERT INTO elementos(nombre, precio, stock)
                        VALUES(?,?,?)''', (nnombre, nprecio, nstock))
        baseDeDatos.commit()