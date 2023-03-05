from class_grammaire import Grammaire
from tkinter import *

new = Grammaire()

app = Tk()
app.title("Analyseur Syntaxique")
app.geometry("750x150")

titre = Label(app,text="Analyseur mini Langage C", font=("Open Sans", 35))
titre.pack()

chaine = Label(app,text="Veuillez saisir la chaine à analyser", font=("Open Sans", 15))
chaine.pack()

e = Entry(app,width=50)
e.pack()

def get_chaine():
  chaine = e.get()
  new.analyseur(chaine)

btn= Button(app,text="Commencer l'analyse", font=("Open Sans",10 ), command = get_chaine)
btn.pack()

app.mainloop()