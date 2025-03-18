import sqlite3
#Conexão com o banco
conn = sqlite3.connect("dbloja.db")

print("Excluir Produto: ")
vcodigo = input("Codigo: ")

# Query parametrizada - enviando intrução sql para ser executada
conn.execute("delete from produto where codprod = ?;", (vcodigo,))
conn.commit()
conn.close()
quit()


