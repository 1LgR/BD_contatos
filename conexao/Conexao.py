import psycopg2
from psycopg2 import sql
from psycopg2 import OperationalError
from modelos.Contatos import Contatos


class Conexao:
    
    def __init__(self, nome_db, usuario, senha, host, porta):
        self.nome_db = nome_db
        self.usuario = usuario
        self.senha = senha
        self.host = host
        self.porta = porta
        self.conexao = None

    def conectar(self):
        try:
            self.conexao = psycopg2.connect(
                database=self.nome_db,
                user=self.usuario,
                password=self.senha,
                host=self.host,
                port=self.porta
            )
            print("Conexão ao banco de dados PostgreSQL realizada com sucesso")
        except OperationalError as e:
            print(f"Ocorreu um erro ao conectar ao banco de dados: {e}")


    def listar_contatos(self):
        if self.conexao is None:
            print("Não há conexão com o banco de dados.")
            return []

        try:
            cursor = self.conexao.cursor()
            query = """
                SELECT * FROM contatos
            """
            cursor.execute(query)
            resultSet = cursor.fetchall()
            contatos = []
            for row in resultSet: 
                contatos.append(Contatos(id=row[0], nome=row[1], apelido=row[2], telefone=row[3], email=row[4]))
            cursor.close()
            return contatos
        except OperationalError as e:
            print(f"Ocorreu um erro ao consultar os contatos: {e}")
            return []
        
        
    def listar_contato(self, contato_id):
        if self.conexao is None:
            print("Não há conexão com o banco de dados.")
            return []

        try:
            cursor = self.conexao.cursor()
            query = """
                SELECT *
                FROM contatos
                WHERE contatos.id = %s
            """
            cursor.execute(query, (contato_id,))
            resultSet = cursor.fetchone()
            contato = (Contatos(id=resultSet[0], nome=resultSet[1], apelido=resultSet[2], telefone=resultSet[3], email=resultSet[4]))
            cursor.close()
            return contato
        except OperationalError as e:
            print(f"Ocorreu um erro ao consultar o contato: {e}")
            return []
        
        
    def adicionar_contato(self, nome, apelido, telefone, email):
        if self.conexao is None:
            print("Não há conexão com o banco de dados.")
            return []

        try:
            cursor = self.conexao.cursor()
            query = """
                INSERT INTO contatos(nome, apelido, telefone, email) VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (nome,apelido,telefone,email))
            return ("Contato Adicionado")
        except OperationalError as e:
            print(f"Ocorreu um erro ao adicionar o contato: {e}")
            return []
        
    def Editar_contato(self, contato):
        if self.conexao is None:
            print("Não há conexão com o banco de dados.")
            return []

        try:
            cursor = self.conexao.cursor()
            query = """
                UPDATE contatos SET nome = %s, apelido = %s, telefone = %s, email = %s Where id = %s
            """
            cursor.execute(query, (contato.nome, contato.apelido, contato.telefone, contato.email, contato.id))
            self.conexao.commit()
            cursor.close
            return ("Contato Editado")
        except OperationalError as e:
            print(f"Ocorreu um erro ao editar o contato: {e}")
            return []
        
    def Deletar_contato(self, contato_id):
        if self.conexao is None:
            print("Não há conexão com o banco de dados.")
            return []

        try:
            cursor = self.conexao.cursor()
            query = """
                DELETE FROM contatos WHERE id = %s
            """
            cursor.execute(query, (contato_id,))
            self.conexao.commit()
            cursor.close()
            return ("Contato Deletado")
        except OperationalError as e:
            print(f"Ocorreu um erro ao deletar o contato: {e}")
            return []