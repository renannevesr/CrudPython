import mysql.connector

''' comandos SQL
create database Vendas;
CREATE TABLE vendas (
  id_produto int(8) unsigned NOT NULL auto_increment,
  nome_produto varchar(255),
  valor int(255),
  PRIMARY KEY (id_produto)
) AUTO_INCREMENT=1;
'''

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='dev1234',
    database='crud',
)
# executar a coneção com o mysql
cursor = conexao.cursor()


def create():
    nome_produto = input(" Nome do produto cadastrado:")
    valor_produto = input(" Valor do produto cadastrado:")
    query = f"INSERT INTO vendas (nome_produto, valor) VALUES ('{nome_produto}','{valor_produto}')"
    cursor.execute(query)
    conexao.commit()  # edita o banco de dados


def read():
    query = "SELECT * FROM vendas"
    cursor.execute(query)
    leitura = cursor.fetchall()  # leitura do banco de dados
    cod = leitura[0]
    cod = list(cod)  # transformando a tupla em lista
    print("Codigo:", cod[0], " Produto:", cod[1], " Valor:", cod[2])


def update():
    nome_produto = input(" Nome do produto a ser alterado:")
    valor_produto = input(" Novo valor do produto:")
    query = f"UPDATE vendas SET valor = {valor_produto} WHERE nome_produto = '{nome_produto}'"
    cursor.execute(query)
    conexao.commit()


def delete():
    nome_produto = input(" Nome do produto a ser deletado:")
    query = f"DELETE FROM vendas WHERE nome_produto = '{nome_produto}'"
    cursor.execute(query)
    conexao.commit()


def saida():  # fechando as conexoes
    cursor.close()
    conexao.close()


# create()
# read()
update()
saida()
