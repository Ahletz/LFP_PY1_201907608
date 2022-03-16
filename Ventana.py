from tkinter import *
from tkinter import filedialog
import tkinter

from Analizador import *

class Grafica:

    direccion = '' #varible con la ubicacion del archivo 

    def __init__(self) :

        print('COMENZANDO PROGRAMA...')

    #Metodo para abrir un archivo 
    def AbrirArchivo(self):
        archivo = filedialog.askopenfilename(title="Abrir",initialdir="C:/")
        direccion= archivo
    
    def Ventana(self):

        ventana = Tk()
        ventana.geometry('900x600') #ventana 
        ventana.configure(background='dark orchid') #color de la ventana 

        lista = ['Reporte de Tokens','Reporte de Erroes','Manual de usuario', 'Manueal Tecnico'] #lsita de opciones
        
        bar = StringVar(ventana) #coponenetes para lista menu 
        bar.set('Reporte de Tokens') #Seleccion por defecto 
        menu = OptionMenu(ventana,bar,*lista).place(x=500,y=10) #Menu generado en lista en la interfaz
         
        self.Botones()
      
        ventana.mainloop()


    def Botones (self):

        llamado = Analisis()

        boton1 = Button(text='Abrir Archivo',command=self.AbrirArchivo).place(x=10,y=10) #boton de carga de archivos
        boton2 = Button(text='Analizar Archivo',command=llamado.Read).place(x=200,y=10)
        boton3 = Button(text='Generar').place(x=650,y=12)

   

        