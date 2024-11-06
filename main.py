from conexao.Conexao import Conexao
from modelos.Contatos import Contatos

conn = Conexao("agenda_contato", "postgres", "postgres", "localhost", "5432")
conn.conectar()

# Exemplo de uso das funções
if __name__ == "__main__":

    while(True):
        #Menu com funções
        print("1 - Listar todos os contatos")
        print("2 - Listar um contato especifico") 
        print("3 - Adicionar um contato")
        print("4 - Editar um contato")
        print("5 - Apagar um contato")      
        print("0 - Sair")
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1:                        
            if conn:
                contatos = conn.listar_contatos()
                for contato in contatos:
                    print(contato)
        elif opcao == 2:
            contato_id = int(input("Digite o ID do Contato desejado: "))                        
            if conn:
                contato = conn.listar_contato(contato_id)
                print(contato)
        elif opcao == 3:
            print("Digite os dados do contato: ")                        
            nome = input("Digite o nome do contato: ")
            apelido = input("Digite o apelido do contato: ")
            telefone = input("Digite o telefone do contato: ")
            email = input("Digite o email do contato: ")
            if conn:
                adicionar = conn.adicionar_contato(nome, apelido, telefone, email)
                print(adicionar)
        elif opcao == 4:
            print("Digite os dados do contato: ")
            id = input("Digite o id do contato: ")                        
            nome = input("Digite o nome do contato: ")
            apelido = input("Digite o apelido do contato: ")
            telefone = input("Digite o telefone do contato: ")
            email = input("Digite o email do contato: ")
            contato = Contatos(id, nome, apelido, telefone, email)
            if conn:
                adicionar = conn.Editar_contato(contato)
                print(adicionar)
        elif opcao == 5:
            print("Digite os dados do contato: ")
            contato_id = int(input("Digite o id do contato: "))                
            if conn:
                deletar = conn.Deletar_contato(contato_id)
                print(deletar)
        elif opcao == 0:
            break
        else:
            print("Opção inválida")