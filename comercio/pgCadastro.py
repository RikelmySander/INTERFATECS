import sqlite3
#Conexão com o banco
conn = sqlite3.connect("dbloja.db")

while True:
    print("Cadastro")
    vcodigo = input("Codigo: ")
    vproduto = input("Produto: ")
    vsaldo = input("Saldo: ")
    vsaldomin = input("Saldo Minimo: ")
    vprecodovenda = input("Preço de venda: ")
    vprecocusto = input("Preço de custo: ")
# Query parametrizada - enviando intrução sql para ser executada
    conn.execute('''insert into produto values (?,?,?,?,?,?)''',
             (vcodigo, vproduto, vsaldo, vsaldomin,vprecodovenda, vprecocusto))
    conn.commit()
    break
conn.close()
quit()


