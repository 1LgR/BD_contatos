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
            cursor.execute(query, (contatos,))
            resultSet = cursor.fetchall()
            pedidos = []
            for row in resultSet: 
                pedidos.append(Contatos(row[0], row[1], row[2], row[3], row[4]))
            cursor.close()
            return pedidos
        except OperationalError as e:
            print(f"Ocorreu um erro ao consultar os pedidos: {e}")
            return []
        
        
    # def obter_itens_por_pedido(self, pedido_id):
    #     if self.conexao is None:
    #         print("Não há conexão com o banco de dados.")
    #         return []

    #     try:
    #         cursor = self.conexao.cursor()
    #         query = """
    #             SELECT itens.nome, itens_pedido.quantidade, itens_pedido.preco_unitario
    #             FROM itens_pedido
    #             JOIN itens ON itens_pedido.item_id = itens.id
    #             WHERE itens_pedido.pedido_id = %s
    #         """
    #         cursor.execute(query, (pedido_id,))
    #         resultSet = cursor.fetchall()
    #         itens = []
    #         for row in resultSet:
    #             itens.append(Item(None, row[0], None, row[1], None))
    #         cursor.close()
    #         return itens
    #     except OperationalError as e:
    #         print(f"Ocorreu um erro ao consultar os itens do pedido: {e}")
    #         return []
        
        
    # def obter_clientes_por_data(self, data_inicio, data_fim):
    #     if self.conexao is None:
    #         print("Não há conexão com o banco de dados.")
    #         return []

    #     try:
    #         cursor = self.conexao.cursor()
    #         query = """
    #             SELECT DISTINCT clientes.*
    #                 FROM clientes
    #                 JOIN pedidos ON clientes.id = pedidos.cliente_id
    #                 WHERE pedidos.data_pedido BETWEEN %s AND %s
    #         """
    #         cursor.execute(query, (data_inicio,data_fim,))
    #         resultSet = cursor.fetchall()
    #         clientes = []
    #         for row in resultSet:
    #             clientes.append(Cliente(row[0], row[1], row[2], row[3], row[4]))
    #         cursor.close()
    #         return clientes
    #     except OperationalError as e:
    #         print(f"Ocorreu um erro ao consultar os itens do pedido: {e}")
    #         return []