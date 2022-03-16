
class Token:

    def Contruccion(self, tipo, palabra, linea, columna): #contructor de tocken 

        a1 = 'Tokent tipo: '
        a2 = ' Token: '
        a3 = ' Linea: '
        a4 = ' Columna: '

        token = a1 + tipo + a2 + palabra + a3 + str(linea) + a4 + str(columna) #contruccion del tocken 

        self.lista.append(token) #agregar a la lista de tockens 
        

    def Lista(self): #agrega cada tocken a una lista 

        self.lista = [] # lista de errores 



        

