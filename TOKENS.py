
from numpy import append
from flask import Flask, render_template


class Token:

    lista = []

    def Lista(self):

        self.lista = []

    def Contruccion(self, tipo, palabra, linea, columna): #contructor de tocken 

        a1 = 'Tokent tipo: ( '
        a2 = ' ) Token: "'
        a3 = '" Linea: '
        a4 = ' Columna: '

        token = a1 + tipo + a2 + palabra + a3 + str(linea) + a4 + str(columna) #contruccion del tocken 

        self.lista.append(token)

    def Reporte(self):

        #inicio de thml
         
        inicio = '<!doctype html><html lang="en"> <head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous"><title>TOKENS</title></head><body><script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script><h1>Lista de Tokens</h1><table class="table"><thead><tr><th scope="col">Tokens: </th></tr></thead><tbody>'

        #final html

        final = '</tbody></body></html>'
        #contenido de html

        contenido = ''

        for i in range (len (self.lista)): #agregar a la tabla los respectivos tokens 

            tokenn = '<tr>' + '<td>' +self.lista[i] + '</td>' +'</tr>'

            contenido += tokenn

        texto = inicio + contenido + final

        op = open('reporte1.html','w')

        op.write(texto)

        op.close()

        
        

        
        

        
        

    



        

