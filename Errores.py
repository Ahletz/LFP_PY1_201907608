class Error:


    lista = []

    def Lista(self):

         self.lista = [] # lista de errores

    def Err(self, palabra, linea, columna):

        a1 = 'Erorr: '
        a2 = ' ,Linea: '
        a3 = ' ,Columna: '

        error = a1 + palabra + a2 + str(linea) + a3 + str(columna) #contrucccion de un error

        self.lista.append(error) #agregar error a la lista

    def Reporte(self):

        #inicio de thml
         
        inicio = '<!doctype html><html lang="en"> <head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous"><title>ERRORES</title></head><body><script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script><h1>Lista de Errores</h1><table class="table"><thead><tr><th scope="col">Errores: </th></tr></thead><tbody>'

        #final html

        final = '</tbody></body></html>'
        #contenido de html

        contenido = ''

        for i in range (len (self.lista)): #agregar a la tabla los respectivos errores 

            error = '<tr>' + '<td>' +self.lista[i] + '</td>' +'</tr>'

            contenido += error

        texto = inicio + contenido + final

        op = open('reporte2.html','w')

        op.write(texto)

        op.close()

    