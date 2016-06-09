#Importaciones necesarias...
from tkinter import *
import tkinter.messagebox

def Suma():
   n1=float(caja1.get())
   n2=float(caja2.get())
   resultado=n1+n2
   tkinter.messagebox.showinfo("Mensaje","El resultado es: %.2f"%resultado)
   caja1.delete(0,20)
   caja2.delete(0,20)

def Resta():
   n1=float(caja1.get())
   n2=float(caja2.get())
   resultado=n1-n2
   tkinter.messagebox.showinfo("Mensaje","El resultado es: %.2f"%resultado)
   caja1.delete(0,20)
   caja2.delete(0,20)

def Multiplicacion():
   n1=float(caja1.get())
   n2=float(caja2.get())
   resultado=n1*n2
   tkinter.messagebox.showinfo("Mensaje","El resultado es: %.2f"%resultado)
   caja1.delete(0,20)
   caja2.delete(0,20)

def Division():
   n1=float(caja1.get())
   n2=float(caja2.get())
   if (n2==0):
      tkinter.messagebox.showinfo("Mensaje","No existse division para cero")
   else:
      resultado=n1/n2
      tkinter.messagebox.showinfo("Mensaje","El resultado es: %.2f"%resultado)
   caja1.delete(0,20)
   caja2.delete(0,20)

app = Tk()
app.title("Calculadora Basica")
app.geometry("400x250+400+200")

#Creacion de una etiqueta
var1 = StringVar()
var1.set("Escribe el primer numero:")
label1 = Label(app,textvariable=var1,height = 2)
label1.pack()

#Creacion de una caja de texto para el primer numero
numero1=StringVar()
caja1=Entry(app,bd=4,textvariable=numero1)
caja1.pack()

#Creacion de otra etiqueta
var2 = StringVar()
var2.set("Escribe el segundo numero:")
label2 = Label(app,textvariable=var2,height = 2)
label2.pack()

#Creacion de otra caja de texto para el segundo numero
numero2=StringVar()
caja2=Entry(app,bd=4,textvariable=numero2)
caja2.pack()

boton1 = Button(app, text = "Suma", command = Suma,width=15)
boton1.pack()

boton2 = Button(app, text = "Resta", command = Resta,width=15)
boton2.pack()

boton3 = Button(app, text = "Multiplicacion", command = Multiplicacion,width=15)
boton3.pack()

boton4 = Button(app, text = "Division", command = Division,width=15)
boton4.pack()

app.mainloop()
