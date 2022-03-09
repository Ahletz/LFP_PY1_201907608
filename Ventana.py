import tkinter 

class Grafica:

    def __init__(self) :

        print('COMENZANDO PROGRAMA...')
    
    def Ventana(self):

        ventana = tkinter.Tk()

        ventana.geometry('500x500')
        ventana.configure(background='dark orchid')

        print ('nuevo cambio')


        ventana.mainloop()

        