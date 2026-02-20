from datetime import datetime
import mysql.connector

#conecte seu BD aqui
conexao = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '2005',
        database = 'bdprojeto',
)

cursor = conexao.cursor()

#Função para imprimir o menu no terminal:
def menu():
    print(
        "\n ===MENU==="
        "\nDigite 1 para adicionar um novo usuário"
        "\nDigite 2 para exibir lista de usuários"
        "\nDigite 3 para excluir os dados de um usuário"
        "\nDigite 4 para atualizar registros"
        "\nDigite 5 para encerrar o programa"
        "\n============"
    ) 

def ler_opcao():
    return input("Por favor, digite uma opção: ")

#Função utilizada para adicionar um novo usuário ao banco
def adicionar_usuario():
    nome = input("Digite o nome do usuário: ")
    cpf = input("Digite o CPF do usuário: ")

    #Formatação do CPF, faz com que no banco, o CPF tenha apenas números
    cpf = "".join(filter(str.isdigit, cpf))
    
    #Impede o CPF de ter mais de 11 dígitos.
    if len(cpf) != 11:
        print("CPF inválido.")
        return None

    data_digitada = input("Digite a data de nascimento no formato DD/MM/AAAA : ")

    #Formatação para que o usuário possa inserir a data no padrão brasileiro
    try:
        data_nascimento = datetime.strptime(data_digitada, "%d/%m/%Y").date()
    except ValueError:
        print("Data inválida.")    
        return None
    
    return nome, cpf, data_nascimento 

#Função utilizada para excluir um usuário
def excluir_usuario():
    #Tratamento de erro: Caso o usuário digite uma letra no lugar de um número, recebera um aviso de erro
    try:
        id_usuario = int(input("Por favor, digite o ID do usuário que deseja excluir: "))
    except ValueError:
        print("O ID digitado não é válido. o ID deve conter apenas dígitos.")
        return None

    return id_usuario       

#Função utilizada para atualizar os dados de um usuário
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
            nova_data = datetime.strptime(nova_data_digitada, "%d/%m/%Y").date()
        except ValueError:
            print("Data inválida.")
            return None    

        return id_usuario, novo_usuario, novo_cpf, nova_data    

#Loop condicional. O código irá repetir até que a opção de encerrar o sistema seja escolhida
while True:
    menu()
    opcao = ler_opcao()
    
    if opcao == '1':
        #Adicionamos uma variável "dados" para caso seja necessário haver algum tratamento de dados.
        dados = adicionar_usuario()

        #Se em algum momento, algum valor inválido seja inserido: retornara None, fazendo com que o programa não prossiga com dados inválidos
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
                
                #cursor.rowcount é responsável por "contar" quantas linhas foram atualizadas no banco, caso nada seja atualizado, retorna um aviso de que não foi possível realizar a alteração 
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