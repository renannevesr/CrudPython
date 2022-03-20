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


cursor.close()
conexao.close()
