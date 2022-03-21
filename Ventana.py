from asyncore import read
from operator import le
from tkinter import *
from tkinter import filedialog
import tkinter
from click import command

from Analizador import Lectura

import webbrowser # abrir documentos en linea


class Grafica:

    direccion = '' #varible con la ubicacion del archivo 
    text = ''
    seleccion = ''

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
        self.seleccion = bar

        mensaje = Text(ventana, background="white", width=100, height=25)

        mensaje.place(x=50, y=70)
        mensaje.insert("insert",'BIENVENIDO')
         
        self.Botones()
      
        ventana.mainloop()


    def Botones (self):

        boton1 = Button(text='Abrir Archivo',command=self.AbrirArchivo).place(x=10,y=10) #boton de carga de archivos
        boton2 = Button(text='Analizar Archivo',command=self.Texto).place(x=200,y=10) #boton muestra en ventana de texto la estructura 
        boton3 = Button(text='Generar Formulario', command=self.Comienzo).place(x=350,y=10) #boton para generar el formulario y comenzar analisis 
        boton4 = Button(text='Generar',command=self.Reporte_tokens).place(x=650,y=12) # boton para generar reportes y manuales

    def Texto (self):

        texto = open(self.direccion) #obtiene direccion

        contenido = texto.read() # lee el contenido de una direccion

        mensaje = Text(background="white", width=100, height=25) ## muestra el cuadro de texto con el documento 
        mensaje.place(x=50, y=70)
        mensaje.insert("insert",contenido) #agrega e insrta el contenido del documento 

        self.text = mensaje.get("1.0", "end") #obtiene los cambios realizados 

    def Comienzo (self):

        llamdo = Lectura()

        llamdo.Read(self.text)


        inicio = '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>FORMULARIO</title></head><bodyb><H1>FORMULARIO LFYP</H1><form action="">'
        cuerpo = ''
        final = '</form></body></html>'

        for i in range(len(llamdo.Objetos)):

            cosas = llamdo.Objetos[i]

            if cosas[0] == 'etiqueta':

                p1 = '<label for="">' 
                cont = cosas[1]
                f1 = '</label>'

                texto = p1 + cont + f1 #creacion label
                cuerpo += texto



            elif cosas[0] == 'texto':

                p1 = '<input type="text" name="name" placeholder="'
                cont = cosas[2]
                f1 = '">'

                texto = p1 + cont + f1 #creacion label
                cuerpo += texto #agrear al form

            elif cosas[0] == 'grupo-radio':
                
                p1 = '<label><input type="checkbox" id="cbox1" value="first_checkbox">'
                f1 = '</label><br>'

                mini = cosas[2]

                for i in range(len(mini)):

                    cont = mini[i]

                    texto = p1 + cont + f1 #creacion label
                    cuerpo += texto #agrear al form


            elif cosas[0] == 'grupo-option':
                
                p1 = '<label for="">' + cosas[1] + '</label><select name="select">'
                f1 = '</select>'
                cont = ''

                mini = cosas[2]

                for i in range(len(mini)):

                    selecciones = '<option value="">' + mini[i] + '</option>'

                    cont += selecciones

                texto = p1 + cont + f1 #creacion label
                cuerpo += texto #agrear al form



            elif cosas[0] == 'boton':

                p1 = '<button>'
                cont = cosas[2]
                f1 = '</button>'

                texto = p1 + cont + f1 #creacion label
                cuerpo += texto #agrear al form


            else:
                
                print('NO ')


        formu = inicio + cuerpo + final

        op = open('formulario.html','w')

        op.write(formu)

        op.close()

        webbrowser.open('formulario.html')



    def Reporte_tokens(self):

        webbrowser.open('reporte1.html')
        webbrowser.open('reporte2.html')

        if self.seleccion == 'Reporte de Tokens':

             webbrowser.open('reporte1.html')

        elif self.seleccion == 'Reporte de Erroes':

            webbrowser.open('reporte2.html')

        else: 

            print('')






        









    

        

        


    
   

        