# calculadora-linux
Script em Python executado via Shell Script no Linux

# Calculadora em Python com Shell Script

Este projeto consiste em uma calculadora desenvolvida em Python que é executada automaticamente através de um script Shell (.sh) em ambiente Linux.

## Requisitos

- Sistema Linux
- Python 3 instalado

Para verificar se o Python está instalado:

```bash
python3 --version
```


## Como executar o projeto

**1.** Baixe os arquivos do repositório:
```bash
https://github.com/joseaugustodossantos64-hash/calculadora-linux.git
```

**2.** Acesse a pasta do projeto:
```bash
cd calculadora-linux
```

**3.** Dê permissão de execução ao script:
```bash
chmod 744 calculadora.sh
```

**4.** Execute o script:
```bash
./calculadora.sh
```

O script irá executar automaticamente o programa Python da calculadora.

## Explicação do funcionamento

O projeto possui dois arquivos principais:

**calculadora.py**

Arquivo responsável pela lógica da calculadora.
Ele realiza operações matemáticas básicas conforme a entrada do usuário.

**calculadora.sh**

Script Shell responsável por executar o arquivo Python automaticamente.

Conteúdo do script:
```bash
#!/bin/bash
python3 calculadora.py
```

Este script permite que o usuário execute a calculadora com apenas um comando no terminal.

## Objetivo

Este projeto foi desenvolvido como prática de:

- Linux
- Shell Script
- Integração Python
- Git e GitHub

## Autor
José Augusto dos Santos
