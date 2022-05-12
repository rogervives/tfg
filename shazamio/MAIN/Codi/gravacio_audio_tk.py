from tkinter import Tk,Label,Button,filedialog,Entry,StringVar,messagebox
import glob
import os
import threading
import pyaudio
import wave

#   Crear finestra
finestra = Tk()
finestra.title("Gravadora d'àudio mp3")

#   Variables inicials
direcotri_actual = StringVar()
gravant = False
reproduint = False
CHUNK = 1024
data = ""
stream = ""
audio = pyaudio.PyAudio()
f = ""

#   Cronòmetre
time = Label(finestra, fg='green', width=20,
             text="00:00:00", bg="black",
             font=("", "30"))
time.place(x=10, y=20)
finestra.geometry("488x97")

#   Botons
btnIniciar = Button(finestra, fg='blue', width=16,
                    text='Gravar', command=iniciar)
btnIniciar.place(x=122,y=71)
btnParar = Button(finestra, fg='blue', width=16,
                  text='Parar', command=parar)
btnParar.place(x=244,y=71)
btnDir = Button(finestra, text='Carpeta',
                width=16, command=direc)
btnDir.place(x=0,y=71)
btnObrir = Button(finestra, text='Obrir', width=16,
                  command=obrir)
btnObrir.place(x=366,y=71)

etDir = Entry(finestra, width=77, bg='lavender',
              textvariable=direcotri_actual)
etDir.place(x=10,y=0)

dire()

finestra.mainloop()