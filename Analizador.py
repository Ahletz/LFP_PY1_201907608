

from Errores import *
from TOKENS import *
from pyparsing import alphanums


class Analisis:



    def Read(self):

        
        texto = open('prueba01.form') #abrir documento y obtener direccion

        contenido = texto.read() #contenido del docmuneto 

        contenido += '#' #agregar finalizador de texto 

        estado = 0 #estado de analizador

        linea = 0 #linea donde se encuentra el analizador

        token = Token()

        error = Error()


        for i in range(len(contenido)):

            if contenido[i] == '\n':

                columna +=1


            if estado == 0:

                if contenido[i].isalpha():
                    palabra += contenido[i]
                    tipo = 'Palabra'
                    continue

                elif contenido[i] == '~':
                    estado = 1 #cambio de estado 

                    #agregar anterior a tockens 
                    token.Contruccion(tipo, palabra, linea, i) # agregar a los tockens
                    
                    palabra += contenido[i]
                    tipo = 'Virgulilla'
                    continue

                elif contenido[i] == ' ':

                    continue #si vienen espacio 

                else: 
                    
                    palabra += contenido[i] #para manejo de errores

                    error.Err(palabra, linea, i)


                    continue
            
            elif estado == 1:

                if contenido[i] == '>':

                    palabra += contenido[i]
                    continue

                elif contenido[i] == '[':

                    estado = 2 #cambio de estado 
                    palabra += contenido[i]
                    continue
                elif contenido[i] == ' ':

                    continue #si vienen espacio 

                else: 
                    
                    palabra += contenido[i] #para manejo de errores
                    continue
            
            elif estado == 2:

                if contenido[i] == '<':

                    estado = 2 #cambio de estado
                    palabra += contenido[i]
                    continue

                elif contenido[i] == ' ':

                    continue #si vienen espacio 

                else: 
                    
                    palabra += contenido[i] #para manejo de errores
                    continue
            
            elif estado == 3:

                if contenido[i].isalpha():
 
                    palabra += contenido[i]
                    continue
                elif contenido[i] == ' ':

                    continue #si vienen espacio 

                else: 
                    
                    palabra += contenido[i] #para manejo de errores
                    continue

                















            








