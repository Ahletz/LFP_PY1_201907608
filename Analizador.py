

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

        columna = 0

        token = Token()

        error = Error()


        for i in range(len(contenido)):

            if contenido[i] == '\n':

                linea  +=1
                columna = 0
                
            columna +=1


            if estado == 0:

                if contenido[i].isalpha():
                    palabra += contenido[i]
                    tipo = 'Palabra'
                    continue

                elif contenido[i] == '~':
                    
                    if palabra.lower().lstrip().rstrip() == 'formulario': #comprobar que si sea una palabra reservada
                        ##agregar la palabra a la lista de tokens
                        columna_palabra = columna -1 #columna e la palabra
                        #agregar anterior a tockens 
                        token.Contruccion(tipo, palabra, linea, columna_palabra) # agregar a los tockens la palabra
                    else:
                        columna_palabra = columna -1
                        error.Err(palabra, linea, columna_palabra) # agregar palabra a lista de errores

                    estado = 1
                    #para virgulilla
                    palabra = '' #limpiar palabra
                    palabra += contenido[i]
                    tipo = 'Virgulilla'

                    token.Contruccion(tipo, palabra, linea, columna) # agregar la virgulilla a lista de tokens

                    continue

                elif contenido[i] == ' ':

                    continue #si vienen espacio 

                else: 
                    
                    palabra += contenido[i] #para manejo de errores

                    error.Err(palabra, linea, columna) # agregar palabra a lista de errores


                    continue
            
            elif estado == 1:

                if contenido[i] == '>':

                    palabra = '' #limpiar palabra
                    palabra += contenido[i]
                    tipo = 'Mayor Que'
                    token.Contruccion(tipo, palabra, linea, columna) # agregar virgulilla
                    continue

                elif contenido[i] == '[':

                    palabra = ''#limpiar palabra
                    estado = 2 #cambio de estado 
                    palabra += contenido[i]
                    tipo = 'Abrir Corchete'
                    token.Contruccion(tipo, palabra, linea, columna) # agregar abrir corchete
                    continue
                elif contenido[i] == ' ':

                    continue #si vienen espacio 

                else: 

                    palabra = '' #limpiar palabra
                    palabra += contenido[i] #para manejo de errores
                    error.Err(palabra, linea, columna) # agregar palabra a lista de errores
                    continue
            
            elif estado == 2:

                if contenido[i] == '<':

                    palabra = '' #limpiar palabra
                    estado = 3 #cambio de estado
                    palabra += contenido[i]
                    tipo = 'Menor Que'
                    token.Contruccion(tipo, palabra, linea, columna) #agregar menor que 

                    palabra = '' #limpiar palabra siguiente estado 
                    continue

                elif contenido[i] == ' ':

                    continue #si vienen espacio 

                else: 
                    
                    palabra = '' # limpiar palabra
                    palabra += contenido[i] #para manejo de errores
                    error.Err(palabra, linea, columna) # agregar palabra a lista de errores
                    continue
            
            elif estado == 3:

                if contenido[i].isalpha() or contenido[i] == ' ':
 
                    palabra += contenido[i]
                    continue

                
                elif contenido[i] == ':':

                    if palabra.lower().rstrip().lstrip() == 'tipo' or palabra.lower().rstrip().lstrip() == 'Valor' or palabra.lower().rstrip().lstrip() == 'fondo':
                        
                        estado = 4
                        ##agregar la palabra a la lista de tokens
                        columna_palabra = columna -1 #columna e la palabra
                        palabra = palabra.lstrip().rstrip() #palabra sin espacios al final o al inicio 
                        #agregar anterior a tockens 
                        token.Contruccion(tipo, palabra, linea, columna_palabra) # agregar a los tockens la palabra

                    elif palabra.lower().lstrip().rstrip() == 'valores': #para los valores
                        
                        estado = 7
                        ##agregar la palabra a la lista de tokens
                        columna_palabra = columna -1 #columna e la palabra
                        palabra = palabra.lstrip().rstrip() #palabra sin espacios al final o al inicio 
                        #agregar anterior a tockens 
                        token.Contruccion(tipo, palabra, linea, columna_palabra) # agregar a los tockens la palabra

                    elif palabra.lower().lstrip().rstrip() == 'evento': #para los eventos

                        estado = 8
                        ##agregar la palabra a la lista de tokens
                        columna_palabra = columna -1 #columna e la palabra
                        palabra = palabra.lstrip().rstrip() #palabra sin espacios al final o al inicio 
                        #agregar anterior a tockens 
                        token.Contruccion(tipo, palabra, linea, columna_palabra) # agregar a los tockens la palabra

                    else: 
                        columna_palabra = columna -1
                        error.Err(palabra, linea, columna_palabra) # agregar palabra a lista de errores

                    palabra = ''#limpiar palabra
                    palabra += contenido[i]
                    tipo = 'Dos puntos'
                    token.Contruccion(tipo, palabra, linea, columna) #agregar menor que 
                    palabra = '' #limpiar palabra antes de entrar 

                else: 
                    
                    palabra = '' #limpiar palabra
                    palabra += contenido[i] #para manejo de errores
                    error.Err(palabra, linea, columna) # agregar palabra a lista de errores
                    continue

            elif estado == 4:

                if contenido[i] == '"':
                    
                    estado = 5
                    palabra = '' #lilmpiara palabra 
                    palabra += contenido[i]
                    tipo = 'Comillas'
                    token.Contruccion(tipo, palabra, linea, columna) #agregar comillas 

                elif contenido [i] == ' ':

                    continue #si viene un espacio 

                else: 

                    palabra = '' # limpiar palabra
                    palabra += contenido[i] #para manejo de errores
                    error.Err(palabra, linea, columna) # agregar palabra a lista de errores
                    continue

            elif estado == 5:

                if contenido[i].isalpha or contenido[i] == ' ' or contenido[i] == '-': #leer el contenido dentro de tipo 

                    palabra += contenido[i]
                    tipo = 'Palabra'
                    continue

                elif contenido[i] == '"':

                    ##agregar la palabra a lista de tokens
                    columna_palabra = columna -1 #columna e la palabra
                    palabra = palabra.rstrip().lstrip() #palabra sin espacios al final o inicio
                    #agregar anterior a tockens 
                    token.Contruccion(tipo, palabra, linea, columna_palabra) # agregar a los tockens la palabra

                    palabra = '' #limpiar la palabra
                    palabra += contenido[i] 

                    ##agregar las comillas a la lista de tockens
                    estado = 6
                    token.Contruccion(tipo, palabra, linea, columna) # agregar a los tockens las comilllas 

                else: 
                    
                    palabra = '' # limpiar palabra
                    palabra += contenido[i] #para manejo de errores
                    error.Err(palabra, linea, columna) # agregar palabra a lista de errores
                    continue

            elif estado == 6:

                if contenido[i] == ',':

                    estado = 3
                    palabra = ''
                    palabra += contenido[i]
                    tipo = 'Coma'
                    token.Contruccion(tipo, palabra, linea, columna) # agregar a los tockens la coma

                else:  

                    palabra = '' # limpiar palabra
                    palabra += contenido[i] #para manejo de errores
                    error.Err(palabra, linea, columna) # agregar palabra a lista de errores
                    continue
            
















                















            








