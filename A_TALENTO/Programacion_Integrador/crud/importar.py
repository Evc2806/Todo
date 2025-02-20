import tkinter as tk
from tkinter import messagebox
import sqlite3

class CRUDCliente:
    def __init__(self, root):
        self.root = root
        self.root.title("CRUD Cliente")
        self.root.geometry("400x400")
        self.root.resizable(False, False)

        # Variables
        self.nombre = tk.StringVar()
        self.apellido1 = tk.StringVar()
        self.apellido2 = tk.StringVar()
        self.edad = tk.StringVar()
        self.correo = tk.StringVar()
        self.telefono = tk.StringVar()

        # Título
        self.title_label = tk.Label(root, text="CRUD ", font=('Arial', 14))
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

    def insertar(self):
        conn = sqlite3.connect('clientes.db')
        c = conn.cursor()
        c.execute("INSERT INTO clientes (nombre, apellido1, apellido2, edad, correo, telefono) VALUES (?, ?, ?, ?, ?, ?)",
                  (self.nombre.get(), self.apellido1.get(), self.apellido2.get(), self.edad.get(), self.correo.get(), self.telefono.get()))
        conn.commit()
        conn.close()
        messagebox.showinfo("Insertar", "Cliente insertado")
        self.limpiar()

    def editar(self):
        # Implementar lógica para seleccionar un cliente existente
        messagebox.showinfo("Editar", "Funcionalidad para seleccionar un cliente para editar")

    def actualizar(self):
        # Implementar lógica para actualizar un cliente existente
        messagebox.showinfo("Actualizar", "Cliente actualizado")

    def borrar(self):
        # Implementar lógica para borrar un cliente
        messagebox.showinfo("Borrar", "Cliente borrado")

    def limpiar(self):
        self.nombre.set("")
        self.apellido1.set("")
        self.apellido2.set("")
        self.edad.set("")
        self.correo.set("")
        self.telefono.set("")
        messagebox.showinfo("Limpiar", "Campos limpiados")
      

if __name__ == "__main__":
    root = tk.Tk()
    app = CRUDCliente(root)
    root.mainloop()

