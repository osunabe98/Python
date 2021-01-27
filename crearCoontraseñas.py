#Importacionde distiontos modulos
import random
from tkinter import *
import string
from tkinter import messagebox
from tkinter.ttk import *

def low():
	entry.delete(0, END)
	#Obtener la longitud de la cadena
	length = var1.get()
	lower = "abcdefghijklmnopqrstuwxyz"
	upper = "ABCDEFGHIJKLMNOPQRSTUWXYZabcdefghijklmnopqrstuwxyz"
	digits = """ABCDEFGHIJKLMNOPQRSTUWXYZabcdefghi
	jklmnopqrstuwxyz0123456789!@#$%&*()"""
	password = ""

	if var.get() == 1:
		for i in range(0, length):
			password=password+ ramdon.choice(lower)
		return password
	elif var.get() == 0:
		for i in range(0, length):
			password=password+ ramdon.choice(upper)
		return password
	elif var.get() == 3:
		for i in range(0, length):
			password=password+ ramdon.choice(digits)
		return password
	else:
			messagebox.showwarning('Python Says', ' First Select Any Option')

def copy1():
	ramdon_pswd=entry.get()
	root.clipboard_clear()
	root.clipboard_append(ramdon_pswd)

def generate():
	password1 = low()
	entry.insert(10, password1)

#Crear barra windows
root = Tk()
var = IntVar()
var1 = IntVar()

#Titulo de la barra
root.title("Generador de contraseñas")

#Crear label y entrada a mostrar
Ramdon_password = Label(root, text="Contraseña")
Ramdon_password.grid(row=0)
entry = Entry(root)
entry.grid(row=0, column=1)

#Crear label para la longitud de la contraseña
c_label = Label(root, text="Longitud")
c_label.grid(row=1)

# Crear botones
copy_button = Button(root, text="Copiar", command=copy1)
copy_button.grid(row=0, column=2)
generate_button = Button(root, text="Generar", command=generate)
generate_button.grid(row=0, column=3)
exit_button = Button(root, text="Salir", command=root.quit)
exit_button.grid(row=0, column=4)

#Radio Buttons
radio_low = Radiobutton(root, text="Débil", variable=var, value=1)
radio_low.grid(row=1, column=2, sticky='E')
radio_middle = Radiobutton(root, text="Media", variable=var, value=0)
radio_middle.grid(row=1, column=3, sticky='E')
radio_strong = Radiobutton(root, text="Fuerte", variable=var, value=3)
radio_strong.grid(row=1, column=4, sticky='E')
combo= Combobox(root, textvariable=var1)

#Combo Box para la longitud de tu contraseña
combo['values'] =(8, 9, 10, 11, 12, 13, 14, 15, 16,
				17, 18, 19, 20, 21, 22, 23, 24, 25,
				26, 27, 28, 29, 30, 31, 32, "Longitud")
combo.current(0)
combo.bind('<<ComboboxSelected>>')
combo.grid(column=1, row=1)
root.mainloop()

