from tkinter import *


# Ventana
ventana = Tk()
ventana.title("Calculadora")
ventana.geometry("800x600")
boton = Button(ventana, text="Salir", command=ventana.quit)
boton.pack() # Se usa para mostrar el boton en la ventana
#Icono ventana
ventana.iconbitmap('icon.ico')
ventana.iconbitmap('./calculadora.ico')






#Loop para mantener la ventana activa
ventana.mainloop()
