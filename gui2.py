from distutils.command.clean import clean
from distutils.command.upload import upload
from re import L
from tkinter import *
from tkinter import filedialog
import wavio as wv
import sounddevice as sound
from scipy.io.wavfile import write
import aws_handler
from fpdf import FPDF
import os

root = Tk()
root.title("VoixEnPDF")
root.geometry("500x450")
root.configure(background="#4a4a4a")


def Open_Audio_File():
    root.filename = filedialog.askopenfilename(initialdir="",title="Veuillez choisir votre fichier audio")
    # pdf_text = aws_handler.upload_and_transcribe(root.filename,os.path.basename(root.filename))
    convert_file(os.path.basename(root.filename),"un homme. Je ne suis pas tout à fait satisfait avec le, donc j'ai décidé de changer de librairie pour celle de. Le menu aurait un bouton pour sélectionner un pré enregistrés, puis ensuite courir la reconnaissance vocale et finalement pour nous donner, avec le résultat en important, la librairie Tes quinté Il faut ajouter une grandeur de fenêtres avec la fonction de géométrie, une couleur de bakoung avec configure et une loupe dans laquelle les éléments de la route de roulera reste. Comme le reste, comme le texte, des images est sont ajoutés avec la fonction de Pâques, JQ doit maintenant adapter avec mon projet. Une des premières choses que je dois ajouter est un bouton pour ouvrir. Le fallait explorer.")
    # aws_handler.clean()

def convert_file(filename, text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=10)
    pdf.cell(200, 10, txt=filename, ln=1, align='C')
    pdf.set_auto_page_break(auto=True, margin=15)
    line = 4
    pdf.multi_cell(0,5,txt=text)
    # for i in text.split("."):
    #     if len(i) > 115:
    #         for j in i.split(" "):
    #         pdf.cell(200, 10, txt=j+" " , ln=line, align='L')
    #     pdf.cell(200, 10, txt=i+"."+ str(len(i)) , ln=line, align='L')
    #     line = line+1
    pdf.output("created.pdf")
photo = PhotoImage(file="mic.png")
icon = Label(image=photo, background="#4a4a4a")
icon.pack(padx=5, pady=5)
Label(text="Veuillez Choisir Un Fichier Audio",font="arial 20 bold",background="#4a4a4a",fg="white").pack()

record = Button(root, font="arial 20", text="Browse",bg="#111111",fg="white", border="0",command=Open_Audio_File).pack()
root.mainloop()