string = input('Digitr uma string:')
lista = []
for letra in string:
  
  lista.append(letra)

lista_invertida = lista[::-1]
print(lista_invertida)