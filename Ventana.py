from asyncore import read
from tkinter import *
from tkinter import filedialog
import tkinter
from click import command

from Analizador import *


class Grafica:

    direccion = '' #varible con la ubicacion del archivo 
    text = ''

    def __init__(self) :

        print('COMENZANDO PROGRAMA...')

    #Metodo para abrir un archivo 
    def AbrirArchivo(self):
        archivo = filedialog.askopenfilename(title="Abrir",initialdir="C:/")
        self.direccion = archivo
    
    def Ventana(self):

        ventana = Tk()
        ventana.geometry('900x600') #ventana 
        ventana.configure(background='dark orchid') #color de la ventana 

        lista = ['Reporte de Tokens','Reporte de Erroes','Manual de usuario', 'Manueal Tecnico'] #lsita de opciones
        
        bar = StringVar(ventana) #coponenetes para lista menu 
        bar.set('Reporte de Tokens') #Seleccion por defecto 
        menu = OptionMenu(ventana,bar,*lista).place(x=500,y=10) #Menu generado en lista en la interfaz

        mensaje = Text(ventana, background="white", width=100, height=25)

        mensaje.place(x=50, y=70)
        mensaje.insert("insert",'que pedo cachorrooo')
         
        self.Botones()
      
        ventana.mainloop()


    def Botones (self):

        boton1 = Button(text='Abrir Archivo',command=self.AbrirArchivo).place(x=10,y=10) #boton de carga de archivos
        boton2 = Button(text='Analizar Archivo',command=self.Texto).place(x=200,y=10) #boton muestra en ventana de texto la estructura 
        boton3 = Button(text='Generar Formulario', command=self.Comienzo).place(x=350,y=10) #boton para generar el formulario y comenzar analisis 
        boton4 = Button(text='Generar').place(x=650,y=12) # boton para generar reportes y manuales

    def Texto (self):

        texto = open(self.direccion) #obtiene direccion

        contenido = texto.read() # lee el contenido de una direccion

        mensaje = Text(background="white", width=100, height=25) ## muestra el cuadro de texto con el documento 
        mensaje.place(x=50, y=70)
        mensaje.insert("insert",contenido) #agrega e insrta el contenido del documento 

        self.text = mensaje.get("1.0", "end") #obtiene los cambios realizados 

    def Comienzo (self):

        llamado = Lectura()

        llamado.Read(self.text)

        

        print('uwu')



        









    

        

        


    
   

        