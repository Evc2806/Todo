import tkinter as tk
from tkinter import messagebox, Toplevel
import sqlite3

class CRUDCliente:
    def __init__(self, root):
        self.root = root
        self.root.title("CRUD Cliente")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        # Variables
        self.nombre = tk.StringVar()
        self.apellido1 = tk.StringVar()
        self.apellido2 = tk.StringVar()
        self.edad = tk.StringVar()
        self.correo = tk.StringVar()
        self.telefono = tk.StringVar()

        # Título
        self.title_label = tk.Label(root, text="Clientes", font=('Arial', 14))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Campos de texto
        self.create_input("Nombre", self.nombre, 1)
        self.create_input("Apellido 1", self.apellido1, 2)
        self.create_input("Apellido 2", self.apellido2, 3)
        self.create_input("Edad", self.edad, 4)
        self.create_input("Correo Electrónico", self.correo, 5)
        self.create_input("Teléfono", self.telefono, 6)

        # Botones
        self.create_button("Insertar", self.insertar, 7, 0)
        self.create_button("Editar", self.editar, 7, 1)
        self.create_button("Actualizar", self.actualizar, 8, 0)
        self.create_button("Borrar", self.borrar, 8, 1)
        self.create_button("Limpiar", self.limpiar, 9, 0, 2)
        self.create_button("Mostrar Clientes", self.mostrar_clientes, 10, 0, 2)
        
        

        # Listbox para mostrar clientes
        self.clientes_listbox = tk.Listbox(root)
        self.clientes_listbox.grid(row=11, column=0, columnspan=2, padx=10, pady=5, sticky="we")
        self.cargar_clientes()


    def create_input(self, label_text, variable, row):
        label = tk.Label(self.root, text=label_text)
        label.grid(row=row, column=0, padx=10, pady=5, sticky="e")
        entry = tk.Entry(self.root, textvariable=variable)
        entry.grid(row=row, column=1, padx=10, pady=5, sticky="we")
        self.root.grid_columnconfigure(1, weight=1)

    def create_button(self, text, command, row, column, colspan=1):
        button = tk.Button(self.root, text=text, command=command)
        button.grid(row=row, column=column, padx=10, pady=5, columnspan=colspan, sticky="we")
        self.root.grid_columnconfigure(column, weight=1)

    def cargar_clientes(self):
        # Cargar clientes en el Listbox
        conn = sqlite3.connect('clientes.db')
        c = conn.cursor()
        c.execute("SELECT id, nombre FROM clientes")
        rows = c.fetchall()
        for row in rows:
            self.clientes_listbox.insert(tk.END, f"{row[0]} - {row[1]}")
        conn.close()

    def insertar(self):
        conn = sqlite3.connect('clientes.db')
        c = conn.cursor()
        c.execute("INSERT INTO clientes (nombre, apellido1, apellido2, edad, correo, telefono) VALUES (?, ?, ?, ?, ?, ?)",
                  (self.nombre.get(), self.apellido1.get(), self.apellido2.get(), self.edad.get(), self.correo.get(), self.telefono.get()))
        conn.commit()
        conn.close()
        messagebox.showinfo("Insertar", "Cliente insertado")
        self.limpiar()
        self.clientes_listbox.delete(0, tk.END)
        self.cargar_clientes()

    def editar(self):
        # Obtener el cliente seleccionado
        seleccionado = self.clientes_listbox.get(tk.ACTIVE)
        if seleccionado:
            cliente_id = seleccionado.split(" - ")[0]
            conn = sqlite3.connect('clientes.db')
            c = conn.cursor()
            c.execute("SELECT * FROM clientes WHERE id=?", (cliente_id,))
            cliente = c.fetchone()
            if cliente:
                self.nombre.set(cliente[1])
                self.apellido1.set(cliente[2])
                self.apellido2.set(cliente[3])
                self.edad.set(cliente[4])
                self.correo.set(cliente[5])
                self.telefono.set(cliente[6])
            conn.close()
        else:
            messagebox.showwarning("Editar", "Seleccione un cliente para editar")

    def actualizar(self):
        seleccionado = self.clientes_listbox.get(tk.ACTIVE)
        if seleccionado:
            cliente_id = seleccionado.split(" - ")[0]
            conn = sqlite3.connect('clientes.db')
            c = conn.cursor()
            c.execute("""UPDATE clientes SET nombre=?, apellido1=?, apellido2=?, edad=?, correo=?, telefono=? 
                         WHERE id=?""",
                      (self.nombre.get(), self.apellido1.get(), self.apellido2.get(), self.edad.get(), self.correo.get(), self.telefono.get(), cliente_id))
            conn.commit()
            conn.close()
            messagebox.showinfo("Actualizar", "Cliente actualizado")
            self.limpiar()
            self.clientes_listbox.delete(0, tk.END)
            self.cargar_clientes()
        else:
            messagebox.showwarning("Actualizar", "Seleccione un cliente para actualizar")

    def borrar(self):
        seleccionado = self.clientes_listbox.get(tk.ACTIVE)
        if seleccionado:
            cliente_id = seleccionado.split(" - ")[0]
            conn = sqlite3.connect('clientes.db')
            c = conn.cursor()
            c.execute("DELETE FROM clientes WHERE id=?", (cliente_id,))
            conn.commit()
            conn.close()
            messagebox.showinfo("Borrar", "Cliente borrado")
            self.limpiar()
            self.clientes_listbox.delete(0, tk.END)
            self.cargar_clientes()
        else:
            messagebox.showwarning("Borrar", "Seleccione un cliente para borrar")

    def limpiar(self):
        self.nombre.set("")
        self.apellido1.set("")
        self.apellido2.set("")
        self.edad.set("")
        self.correo.set("")
        self.telefono.set("")
        messagebox.showinfo("Limpiar", "Campos limpiados")

    def mostrar_clientes(self):
        # Crear una nueva ventana para mostrar todos los clientes
        new_window = Toplevel(self.root)
        new_window.title("Lista de Clientes")
        new_window.geometry("400x300")

        listbox = tk.Listbox(new_window)
        listbox.pack(fill=tk.BOTH, expand=True)

        # Cargar todos los clientes en la nueva ventana
        conn = sqlite3.connect('clientes.db')
        c = conn.cursor()
        c.execute("SELECT * FROM clientes")
        rows = c.fetchall()
        for row in rows:
            listbox.insert(tk.END, f"ID: {row[0]}, Nombre: {row[1]}, Apellido1: {row[2]}, Apellido2: {row[3]}, Edad: {row[4]}, Correo: {row[5]}, Teléfono: {row[6]}")
        conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = CRUDCliente(root)
    root.mainloop()
