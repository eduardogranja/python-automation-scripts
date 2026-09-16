import os
import time
os.makedirs('pasta_y', exist_ok=True)
caminho_x= 'pasta_x/dados.txt'
caminho_y= 'pasta_y/dados.txt'
while True:
        if os.path.exists(caminho_x):
            with open(caminho_x, 'r') as arquivo_leitura:
                texto_lido = arquivo_leitura.read()
            numero= texto_lido.split()
            numero1 = int(numero[0])
            numero2 = int(numero[1])
            soma = numero1 + numero2
            with open(caminho_y, 'w') as arquivo:
                arquivo.write(str(soma))
            os.remove(caminho_x)    
        time.sleep(5)