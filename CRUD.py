from datetime import datetime
import mysql.connector

#conecte seu BD aqui
conexao = mysql.connector.connect(
        host = '',
        user = '',
        password = '',
        database = '',
)

cursor = conexao.cursor()

def menu():
    print(
        "\n ===MENU==="
        "\nDigite 1 para adicionar um novo usuário"
        "\nDigite 2 para exibir registros"
        "\nDigite 3 para excluir um usuário"
        "\nDigite 4 para atualizar os dados de um usuário"
        "\nDigite 5 para encerrar o programa"
        "\n============"
    ) 

def ler_opcao():
    return input("Por favor, digite uma opção: ")

def adicionar_usuario():
    nome = input("Digite o nome do usuário: ")
    cpf = input("Digite o CPF do usuário: ")

    cpf = "".join(filter(str.isdigit, cpf))
    
    if len(cpf) != 11:
        print("CPF inválido.")
        return None

    data_digitada = input("Digite a data de nascimento no formato DD/MM/AAAA : ")

    try:
        data_nascimento = datetime.strptime(data_digitada, "%d/%m/%Y").date()
    except ValueError:
        print("Data inválida.")    
        return None
    
    return nome, cpf, data_nascimento 

def excluir_usuario():
    try:
        id_usuario = int(input("Por favor, digite o ID do usuário que deseja excluir: "))
    except ValueError:
        print("O ID digitado esta incorreto.")
        return None

    return id_usuario       

def atualizar_usuario():
    try:
        id_usuario = int(input("Por favor, digite o ID do usuário que deseja alterar os dados: "))
    except ValueError:
        print("O ID digitado esta incorreto.")
        return None
    else:
        novo_usuario = input("Digite os novos dados do usuário: ")
        novo_cpf = input("Digite um novo CPF: ")
        
        novo_cpf = "".join(filter(str.isdigit, novo_cpf))
        if len(novo_cpf) != 11:
            print("CPF inválido.")
            return None
        
        nova_data_digitada = input("Digite uma nova data de nascimento (DD/MM/AAAA): ")

        try:
            nova_data = datetime.strptime(nova_data_digitada, "%d/%m/%Y")
        except ValueError:
            print("Data inválida.")
            return None    

        return id_usuario, novo_usuario, novo_cpf, nova_data    

while True:
    menu()
    opcao = ler_opcao()
    
    if opcao == '1':
        dados = adicionar_usuario()

        if dados is None:
            continue

        nome, cpf, data_nascimento = dados
            
        comando = 'INSERT INTO usuarios (usuario, cpf, data_nascimento) VALUES (%s, %s, %s)'
        valores = (nome, cpf, data_nascimento)
        
        cursor.execute(comando, valores)
        conexao.commit()
        print("Usuário registrado com sucesso!")    
    
    elif opcao == '2':
        comando = 'SELECT * FROM usuarios'

        cursor.execute(comando)
        resultado = cursor.fetchall()
        
        for id_usuario, nome, cpf, data in resultado:
            print(f"ID: {id_usuario} | Nome: {nome} | CPF: {cpf} | Nascimento: {data}")
    
    elif opcao == '3':
            dados = excluir_usuario()

            if dados is None:
                continue
            else:
                id_usuario = dados

                comando = 'DELETE FROM usuarios WHERE idUsuarios = %s'
                valores = (id_usuario,)
                
                cursor.execute(comando, valores)
                conexao.commit()
                
                if cursor.rowcount == 0:
                    print("ID de usuário não encontrado.")
                else:
                    print("O usuário foi deletado com sucesso!")
    elif opcao == '4':
            dados = atualizar_usuario()

            if dados is None:
                continue
            
            id_usuario, novo_usuario, novo_cpf, nova_data = dados
            
            comando = 'UPDATE usuarios SET usuario = %s, cpf = %s, data_nascimento = %s WHERE idUsuarios = %s'
            valores = (novo_usuario, novo_cpf, nova_data, id_usuario,)

            cursor.execute(comando, valores)
            conexao.commit()
             
            if cursor.rowcount == 0:
                print("ID de usuário não encontrado.")
            else:
                print("Usuário alterado com sucesso!")
        
    elif opcao == '5':
        break

    else:
        print("Opção inválida") 

cursor.close()
conexao.close()