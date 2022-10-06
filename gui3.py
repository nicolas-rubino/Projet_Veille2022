import tkinter as tk
from tkinter import filedialog

def New_Window():
    Window = tk.Toplevel()
    canvas = tk.Canvas(Window, height=HEIGHT, width=WIDTH)
    canvas.pack()
    
def Open_Audio_File():
    root.filename = filedialog.askopenfilename(initialdir="",title="Veuillez choisir votre fichier audio")
    

HEIGHT = 300
WIDTH = 500

root = tk.Tk()
root.title("Systeme de reconnaissance vocale")
root.geometry("500x450")
root.configure(background="#4a4a4a")
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

button = tk.Button(root, text="Commencer Enregistrement", bg='White', fg='Black',
                              command=lambda: New_Window())

button2 = tk.Button(root, text="Choisir un fichier audio", bg='White', fg='Black',
                              command=lambda: Open_Audio_File())

button.place(x=50,y=100)
button2.place(x=300,y=100)
root.mainloop()