# CRUD em Python

![MySQL](https://img.shields.io/badge/mysql-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## Descrição
Este foi meu primeiro projeto em Python, um CRUD (Create, Read, Update, Delete) de registro de usuários simples, porem direto e funcional.

O objetivo deste projeto foi aplicar e consolidar os ensinamentos que estive aprendendo no bootcamp Gen-IA e Dados da DIO em parceria com Bradesco.

## Ferramentas utilizadas:
- Python 3
- MySQL

## Funcionalidades:
- Adicionar novo usuário
- Listar usuários cadastrados
- Atualizar dados de um usuário
- Excluir usuário
- Validação de CPF (apenas números e 11 dígitos)
- alidação de data no formato DD/MM/AAAA
- Tratamento de erro para ID inválido

## Utilização:
Caso deseje utilizar o programa, sera necessário instalar:

- MySQL
- Conector Python para MySQL 

instale o conector com o comando:
```bash
 pip install mysql-connector-python
```
Após a instalação  e configuração do banco de dados, sera necessário que o usuário conecte seu banco de dados pessoal ao código. 

Seguindo o exemplo:
```bash
conexao = mysql.connector.connect(
        host = 'localhost',
        user = 'seu_usuario',
        password = 'sua_senha',
        database = 'seu_banco',
)
```

O código ira pedir para que o usuário escolha uma opção

```bash
===MENU=====
Digite 1 para adicionar um novo usuário
Digite 2 para exibir registros
Digite 3 para excluir um usuário
Digite 4 para atualizar os dados de um usuário
Digite 5 para encerrar o programa
============
```
Basta digitar a opção que deseja, após isso, o código entra em um loop até que a opção 5 seja selecionada

#
Projeto desenvolvido com fins educacionais para prática de manipulação de banco de dados utilizando Python.