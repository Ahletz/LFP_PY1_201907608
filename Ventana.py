from tkinter import *

class Grafica:

    def __init__(self) :

        print('COMENZANDO PROGRAMA...')
    
    def Ventana(self):

        ventana = Tk()

        lista = ['Reporte de Tokens','Reporte de Erroes','Manual de usuario', 'Manueal Tecnico']

        ventana.geometry('900x600') #ventana 
        ventana.configure(background='dark orchid') #color de la ventana 
        boton1 = Button(text='Abrir Archivo').place(x=10,y=10) #boton de carga de archivos
        boton2 = Button(text='Analizar Archivo').place(x=200,y=10)
        area_texto= Text(ventana,height=30,width=110).place(x=10,y=60)
        bar = StringVar(ventana) #coponenetes para lista menu 
        bar.set('Reporte de Tokens') #Seleccion por defecto 
        menu = OptionMenu(ventana, bar,*lista).place(x=500,y=10) #Menu generado en lista en la interfaz
        boton3 = Button(text='Gemerar').place(x=650,y=12)
        

        ventana.mainloop()

        