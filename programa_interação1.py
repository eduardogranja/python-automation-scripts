import os
import time
os.makedirs('pasta_x', exist_ok=True)
caminho_x = 'pasta_x/dados.txt'
caminho_y = 'pasta_y/dados.txt'
numero_1 = int(input ('Digite o 1º números: '))
numero_2 = int(input ('Digite o 2º números: '))
with open(caminho_x, 'w') as arquivo:
    arquivo.write(f'{numero_1} {numero_2}')
while not os.path.exists(caminho_y):
    time.sleep(1)
with open(caminho_y, 'r') as arquivo:
    resultado = arquivo.read()
print (resultado)