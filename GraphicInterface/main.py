# Importing libraries
from tkinter import *
import os

c = os.path.dirname(__file__)
filename = c + "\\nomes.txt"

def saveData():
    file = open(filename, "a")
    
    file.write("Nome: %s" % vname.get())
    file.write("\nTelefone: %s" % vphone.get())
    file.write("\nEmail: %s" % vemail.get())
    file.write("\nOBS.: %s" % vobs.get("1.0",END))
    file.write("\n")
    file.close()

app = Tk()
app.title("WKO Teste")
app.geometry("300x500")
app.configure(background="#000000")

# anchor => N, S, E, W -> Norte, Sul, Leste, Oeste
name = Label(app, text="Nome:", background="red", foreground="white", anchor=W)
name.place(x=10, y=10, width=200, height=20)

# Entry -> Usado para uma única linha
vname = Entry(app)
vname.place(x=55, y=12, width=100, height=15)

phone = Label(app, text="Telefone:", background="#0000ff", foreground="white", anchor=W)
phone.place(x=10, y=50, width=200, height=20)

vphone = Entry(app)
vphone.place(x=65, y=52, width=100, height=15)

email = Label(app, text="Email:", background="darkgreen", foreground="white", anchor=W)
email.place(x=10, y=90, width=200, height=20)

vemail = Entry(app)
vemail.place(x=50, y=92, width=150, height=15)

obs = Label(app, text="OBS.:", background="darkgreen", foreground="white", anchor=NW)
obs.place(x=10, y=130, width=200, height=100)

# Text -> Usado para Multilinhas
vobs = Text(app)
vobs.place(x=55, y=132, width=120, height=85)

button = Button(app, text="Enviar", command=saveData)
button.place(x=85, y=372, width=120, height=85)

app.mainloop()