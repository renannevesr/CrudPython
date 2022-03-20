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

# Create
nome_produto = input(" Nome do produto cadastrado:")
valor_produto = input(" Valor do produto cadastrado:")
comando = f"INSERT INTO vendas (nome_produto, valor) VALUES ('{nome_produto}','{valor_produto}')"
cursor.execute(comando)
conexao.commit()  # edita o banco de dados


# fechando as conexoes
cursor.close()
conexao.close()
