from tkinter import*
raiz=Tk()
raiz.title("Esta es mi primera ventana") # t´tulo ventana
raiz.resizable(True,True)# redimencionar a lo alto y ancho tamaño ventana(true, false también funciona)
raiz.geometry("600x650")# tamaño de la raíz pero no del frame y se adapta al tamaño de su contenedor
raiz.config(bg="blue")
miFrame=Frame()# crear frame
miFrame.pack()# empaquetar frame
miFrame.config(bg="red")
miFrame.config(width="540", height="400")
raiz.mainloop()