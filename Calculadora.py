#	PROGRAMA CALCULADORA CON TKINTER
import sys
from Tkinter import *

app=Tk()
app.title("CALCULADORA")

lamina = Frame(app, height=200, width=200) # Creamos un frame en nuestro contenedor app
lamina.pack(padx=10, pady=10)


valor="" # Variable para guardar lo que vayamos escribiendo
texto = Entry (lamina, width=20, font=("Arial", 16),textvariable=valor).place(x=0, y=0)
boton7= Button(lamina, width=4, text="7", font=(16)).place(x=0, y=35)
boton8= Button(lamina, width=4, text="8", font=(16)).place(x=50, y=35)
boton9= Button(lamina, width=4, text="9", font=(16)).place(x=100, y=35)
botonC= Button(lamina, width=4, text="C", font=(16)).place(x=150, y=35)

boton4= Button(lamina, width=4, text="4", font=(16)).place(x=0, y=70)
boton5= Button(lamina, width=4, text="5", font=(16)).place(x=50, y=70)
boton6= Button(lamina, width=4, text="6", font=(16)).place(x=100, y=70)
botonPara= Button(lamina, width=4, text="/", font=(16)).place(x=150, y=70)

boton1= Button(lamina, width=4, text="1", font=(16)).place(x=0, y=105)
boton2= Button(lamina, width=4, text="2", font=(16)).place(x=50, y=105)
boton3= Button(lamina, width=4, text="3", font=(16)).place(x=100, y=105)
botonPor= Button(lamina, width=4, text="*", font=(16)).place(x=150, y=105)

boton0= Button(lamina, width=4, text="0", font=(16)).place(x=0, y=140)
botonComa= Button(lamina, width=4, text=",", font=(16)).place(x=50, y=140)
botonMenos= Button(lamina, width=4, text="-", font=(16)).place(x=100, y=140)
botonMas= Button(lamina, width=4, text="+", font=(16)).place(x=150, y=140)

botonIgual= Button(lamina, width=21, text="=", font=(16)).place(x=0, y=175)

app.mainloop()

