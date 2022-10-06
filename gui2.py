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
    pdf_text = aws_handler.upload_and_transcribe(root.filename,os.path.basename(root.filename))
    convert_file(os.path.basename(root.filename),pdf_text)
    aws_handler.clean()

def convert_file(filename, text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=10)
    pdf.cell(200, 10, txt=filename, ln=1, align='C')
    line = 4
    for i in text.split("."):
        pdf.cell(200, 10, txt=i+".", ln=line, align='L')
        line = line+1
    pdf.output("created.pdf")

photo = PhotoImage(file="mic.png")
icon = Label(image=photo, background="#4a4a4a")
icon.pack(padx=5, pady=5)
Label(text="Veuillez Choisir Un Fichier Audio",font="arial 20 bold",background="#4a4a4a",fg="white").pack()

record = Button(root, font="arial 20", text="Browse",bg="#111111",fg="white", border="0",command=Open_Audio_File).pack()
root.mainloop()