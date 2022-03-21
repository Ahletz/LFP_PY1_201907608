

from Errores import *
from TOKENS import *
from pyparsing import alphanums



class Lectura:

    Objetos = []

    
    def Read(self, texto):

        #texto = open(direccion) #abrir documento y obtener direccion

        contenido = texto #texto.read() #contenido del docmuneto 

        estado = 0 #estado de analizador

        linea = 1 #linea donde se encuentra el analizador

        columna = 1

        palabra = '' #contenedor

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

                elif contenido[i] == ' ' or contenido[i] == '\n' or contenido[i] == '\t':

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
                elif contenido[i] == ' ' or contenido[i] == '\n' or contenido[i] == '\t':

                    continue #si vienen espacio 

                else: 

                    palabra = '' #limpiar palabra
                    palabra += contenido[i] #para manejo de errores
                    error.Err(palabra, linea, columna) # agregar palabra a lista de errores
                    continue
            
            elif estado == 2:

                if contenido[i] == '<':

                    funciones = [] # lista para guardar cada una de las funciones del formulario
                    ListaV = [] #lista con los valores de valores

                    palabra = '' #limpiar palabra
                    estado = 3 #cambio de estado
                    palabra += contenido[i]
                    tipo = 'Menor Que'
                    token.Contruccion(tipo, palabra, linea, columna) #agregar menor que 

                    palabra = '' #limpiar palabra siguiente estado 
                    continue

                elif contenido[i] == ' ' or contenido[i] == '\n' or contenido[i] == '\t':

                    continue #si vienen espacio 

                else: 
                    
                    palabra = '' # limpiar palabra
                    palabra += contenido[i] #para manejo de errores
                    error.Err(palabra, linea, columna) # agregar palabra a lista de errores
                    continue
            
            elif estado == 3:

                if contenido[i].isalpha():
                    tipo = 'palabra Reservada'
                    palabra += contenido[i]
                    continue

                elif contenido[i] == '\n' or contenido[i] == '\t' or contenido[i] == ' ':
                    palabra = ''
                    continue

                elif contenido[i] == ':':
                    
                    

                    if palabra.lower() == 'tipo' or palabra.lower() == 'valor' or palabra.lower() == 'fondo':
                        
                        estado = 4
                        ##agregar la palabra a la lista de tokens
                        columna_palabra = columna -1 #columna e la palabra
                        palabra = palabra.lstrip().rstrip() #palabra sin espacios al final o al inicio 
                        #agregar anterior a tockens 
                        token.Contruccion(tipo, palabra, linea, columna_palabra) # agregar a los tockens la palabra

                    elif palabra.lower().lstrip().rstrip() == 'valores': #para los valores
                        
                        estado = 8
                        ##agregar la palabra a la lista de tokens
                        columna_palabra = columna -1 #columna e la palabra
                        palabra = palabra.lstrip().rstrip() #palabra sin espacios al final o al inicio 
                        #agregar anterior a tockens 
                        token.Contruccion(tipo, palabra, linea, columna_palabra) # agregar a los tockens la palabra

                    elif palabra.lower() == 'evento': #para los eventos

                        estado = 12
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
                    palabra += contenido[i]
                    tipo = 'Comillas'
                    token.Contruccion(tipo, palabra, linea, columna) #agregar comillas 
                    palabra = '' #lilmpiara palabra 

                elif contenido [i] == ' ' or contenido[i] == '\n' or contenido[i] == '\t':

                    continue #si viene un espacio 

                else: 

                    palabra = '' # limpiar palabra
                    palabra += contenido[i] #para manejo de errores
                    error.Err(palabra, linea, columna) # agregar palabra a lista de errores
                    continue

            elif estado == 5:

                if contenido[i].isalpha() or contenido[i] == ' ' or contenido[i] == '-' or contenido[i] == ':': #leer el contenido dentro de tipo 

                    palabra += contenido[i]
                    tipo = 'Palabra'
                    continue

                elif contenido[i] == '\n' or contenido[i] == '\t' :
                    palabra = ''
                    continue

                elif contenido[i] == '"':

                    ##agregar la palabra a lista de tokens
                    columna_palabra = columna -1 #columna e la palabra
                    palabra = palabra.rstrip().lstrip() #palabra sin espacios al final o inicio
                    #agregar anterior a tockens 
                    token.Contruccion(tipo, palabra, linea, columna_palabra) # agregar a los tockens la palabra
                    funciones.append(palabra)

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

                elif contenido[i] == '>':
                    
                    self.Objetos.append(funciones) #agregar palabra a objetos

                    estado = 7
                    palabra = ''
                    palabra += contenido[i]
                    tipo = 'Mayor Que'
                    token.Contruccion(tipo, palabra, linea, columna) # agregar a los tockens la coma

                elif contenido [i] == ' ' or contenido[i] == '\n' or contenido[i] == '\t':

                    continue #si viene un espacio 

                else:  

                    palabra = '' # limpiar palabra
                    palabra += contenido[i] #para manejo de errores
                    error.Err(palabra, linea, columna) # agregar palabra a lista de errores
                    continue

            elif estado == 7:

                if contenido [i] == ',':

                    estado = 2
                    palabra = ''
                    palabra += contenido[i]
                    tipo = 'Coma'
                    token.Contruccion(tipo, palabra, linea, columna) # agregar a los tockens la coma

                elif contenido[i] == '>':

                    self.Objetos.append(funciones)

                    palabra = ''
                    palabra += contenido[i]
                    tipo = 'Mayor Que'
                    token.Contruccion(tipo, palabra, linea, columna) # agregar a los tockens las comillas

                elif contenido[i] == ']':
                    
                    palabra = ''
                    palabra += contenido[i]
                    tipo = 'Cerrar Corchete'
                    token.Contruccion(tipo, palabra, linea, columna) # agregar a los tockens las comillas

                elif contenido [i] == ' ' or contenido[i] == '\n' or contenido[i] == '\t':

                    continue #si viene un espacio 

                else:  

                    palabra = '' # limpiar palabra
                    palabra += contenido[i] #para manejo de errores
                    error.Err(palabra, linea, columna) # agregar palabra a lista de errores
                    continue

            elif estado == 8:

                if contenido[i] == '"':

                    palabra = ''
                    palabra += contenido[i]
                    tipo = 'Comillas'
                    token.Contruccion(tipo, palabra, linea, columna) # agregar a los tockens las comillas
                
                elif contenido[i] == '[':
                    
                    estado = 9
                    palabra = ''
                    palabra += contenido[i]
                    tipo = 'Abrir corchete'
                    token.Contruccion(tipo, palabra, linea, columna) # agregar a los tockens las comillas

                elif contenido [i] == ' ' or contenido[i] == '\n' or contenido[i] == '\t':

                    continue #si viene un espacio 

                else: 

                    palabra = '' # limpiar palabra
                    palabra += contenido[i] #para manejo de errores
                    error.Err(palabra, linea, columna) # agregar palabra a lista de errores
                    continue

            elif estado == 9: 

                if contenido[i] == "'":

                    palabra = ''
                    palabra += contenido[i]
                    tipo = 'Comilla simple'
                    token.Contruccion(tipo, palabra, linea, columna) # agregar a los tockens las comillas
                    estado = 10
                    palabra = '' #limpiar palabra para estado 9 (letras)
                
                elif contenido [i] == ' ' or contenido[i] == '\n' or contenido[i] == '\t':

                    continue #si viene un espacio 

                else: 

                    palabra = '' # limpiar palabra
                    palabra += contenido[i] #para manejo de errores
                    error.Err(palabra, linea, columna) # agregar palabra a lista de errores
                    continue

            elif estado == 10:

                if contenido[i].isalpha() or contenido[i] == ' ':

                    palabra += contenido[i]
                    continue

                elif contenido[i] == '\n' or contenido[i] == '\t' :
                    palabra = ''
                    continue

                elif contenido[i] == "'":

                    ListaV.append(palabra)

                    ##agregar la palabra a lista de tokens
                    columna_palabra = columna -1 #columna e la palabra
                    palabra = palabra.rstrip().lstrip() #palabra sin espacios al final o inicio
                    #agregar anterior a tockens 
                    token.Contruccion(tipo, palabra, linea, columna_palabra) # agregar a los tockens la palabra

                    palabra = ''
                    palabra += contenido[i]
                    tipo = 'Comilla simple'
                    token.Contruccion(tipo, palabra, linea, columna) # agregar a los tockens las comillas
                
                elif contenido[i] == ',':

                    palabra = ''
                    palabra += contenido[i]
                    tipo = 'Coma'
                    token.Contruccion(tipo, palabra, linea, columna) # agregar a los tockens las comillas
                    estado = 9
                
                elif contenido[i] == ']':

                    funciones.append(ListaV) #agregar lista de valores a lista de funciones

                    palabra = ''
                    palabra += contenido[i]
                    tipo = 'Cerrar Corchete'
                    token.Contruccion(tipo, palabra, linea, columna) # agregar a los tockens las comillas
                    estado = 11

                else: 

                    palabra = '' # limpiar palabra
                    palabra += contenido[i] #para manejo de errores
                    error.Err(palabra, linea, columna) # agregar palabra a lista de errores
                    continue

            elif estado == 11:

                if contenido[i] == '>':

                    self.Objetos.append(funciones)

                    palabra = ''
                    palabra += contenido[i]
                    tipo = 'Mayor Que'
                    token.Contruccion(tipo, palabra, linea, columna) # agregar a los tockens la coma
                    estado = 7

                elif contenido [i] == ' ' or contenido[i] == '\n' or contenido[i] == '\t':

                    continue #si viene un espacio 

                else:  

                    palabra = '' # limpiar palabra
                    palabra += contenido[i] #para manejo de errores
                    error.Err(palabra, linea, columna) # agregar palabra a lista de errores
                    continue

            elif estado == 12:

                if contenido[i] == '<':

                    palabra = '' #limpiar palabra
                    estado = 13 #cambio de estado
                    palabra += contenido[i]
                    tipo = 'Menor Que'
                    token.Contruccion(tipo, palabra, linea, columna) #agregar menor que 

                    palabra = '' #limpiar palabra siguiente estado 
                    continue

                elif contenido[i] == ' ' or contenido[i] == '\n' or contenido[i] == '\t':

                    continue #si vienen espacio 

                else: 
                    
                    palabra = '' # limpiar palabra
                    palabra += contenido[i] #para manejo de errores
                    error.Err(palabra, linea, columna) # agregar palabra a lista de errores
                    continue

            elif estado == 13:

                if contenido[i].isalpha() or contenido[i] == ' ':

                    tipo = 'Palabra'
                    palabra += contenido[i]

                    continue

                elif contenido[i] == '\n' or contenido[i] == '\t' :
                    palabra = ''
                    continue


                elif contenido[i] == '>':

                    funciones.append(palabra) #agregar palabra

                    ##agregar la palabra a lista de tokens
                    columna_palabra = columna -1 #columna e la palabra
                    palabra = palabra.rstrip().lstrip() #palabra sin espacios al final o inicio
                    #agregar anterior a tockens 
                    token.Contruccion(tipo, palabra, linea, columna_palabra) # agregar a los tockens la palabra

                    palabra = '' #limpiar palabra
                    estado = 7 #cambio de estado
                    palabra += contenido[i]
                    tipo = 'Mayor Que'
                    token.Contruccion(tipo, palabra, linea, columna) #agregar menor que

                else: 
                    
                    palabra = '' # limpiar palabra
                    palabra += contenido[i] #para manejo de errores
                    error.Err(palabra, linea, columna) # agregar palabra a lista de errores
                    continue

        token.Reporte() #generar el reporte de tockens
        error.Reporte() #generar el reporte de errores

            









                






















                















            








