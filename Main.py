from Analizador import *
from TOKENS import *
from Errores import *

llamado = Analisis()

llamado.Read()

tokens = Token()

error = Error()

lista1 = tokens.lista

lista2 = error.lista

for i in range(len(lista1)):

    print(lista1[i])