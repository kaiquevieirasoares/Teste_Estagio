anterior = 0
proxima =  1
soma = 1
pertence = False

list = []
valor_informado = int(input('Digite o valor para verificação:'))
for n in range(0,valor_informado):
    soma = proxima + anterior
    list.append(soma)
    anterior = proxima
    proxima = soma

i=0
while True:
  
  termo = list[i]
  
  if termo == valor_informado:
    pertence = True
    break
  # Se o termo for maior que o número, sair do laço
  elif termo > valor_informado:
    break
  # Se o termo for menor que o número, incrementar i e continuar o laço
  else:
    i += 1
if pertence:
  print(f"O número {valor_informado} pertence à sequência de Fibonacci.")
else:
  print(f"O número {valor_informado} não pertence à sequência de Fibonacci.")
