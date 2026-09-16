# 🚀 Python Automation Scripts: File-Based Messenger

> Um sistema simples e eficiente de comunicação entre scripts Python utilizando diretórios do sistema como filas de processamento de dados.

## 💻 Sobre o projeto

Este projeto demonstra como criar uma arquitetura onde diferentes scripts operam de forma independente, mas se comunicam através da manipulação de arquivos. O fluxo simula um pipeline de processamento de dados em miniatura.

O sistema é composto por dois processos isolados:
1. Um script gerador que cria informações estruturadas e as deposita em um diretório de entrada (`pasta_x`).
2. Um script consumidor que monitora a entrada, realiza os cálculos necessários com os dados recebidos e armazena os resultados processados em um diretório de saída (`pasta_y`).

### ✨ Funcionalidades

- [x] Geração automática de diretórios de infraestrutura via código.
- [x] Leitura e escrita de arquivos de texto para persistência de dados.
- [x] Separação de responsabilidades (Desacoplamento entre quem gera e quem processa a informação).
- [x] Execução de cálculos baseados em arquivos de input.

## 🛠 Tecnologias utilizadas

- **Python 3**
- **Bibliotecas nativas (OS)** para manipulação do sistema de arquivos.

## 🧠 Desafios e Aprendizados

O principal objetivo deste projeto foi aplicar conceitos de automação e integração do Python com o sistema operacional. 

Utilizei a biblioteca nativa `os`, especificamente o comando `os.makedirs`, para garantir que os diretórios necessários (`pasta_x` e `pasta_y`) fossem criados automaticamente durante a execução, evitando erros de infraestrutura. Além disso, estruturar a comunicação por meio de arquivos exigiu gerenciar corretamente a abertura, leitura, escrita e fechamento de dados, garantindo que a informação não se perdesse ou fosse corrompida entre a etapa de geração e a de cálculo.

## 🚀 Como rodar o projeto localmente

Pré-requisitos: Ter o [Python](https://www.python.org/downloads/) instalado na sua máquina.

### 🎲 Executando os scripts
Clone este repositório
$ git clone https://github.com/eduardogranja/python-automation-scripts.git

Acesse a pasta do projeto no terminal
$ cd python-automation-scripts

1. Execute primeiro o script gerador para criar os dados na pasta_x
$ python programa_interacao1.py

2. Execute o script consumidor para calcular e enviar os resultados para a pasta_y
$ python programa_interacao2.py
