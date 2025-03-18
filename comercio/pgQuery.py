import sqlite3

#Conexão com o banco
conn = sqlite3.connect("dbloja.db")
cursor = conn.cursor()

print("Consultar Produto: ")
vcodigo = input("Codigo: ")
# Query parametrizada - enviando intrução sql para ser executada
cursor.execute("Select codprod, dsprod, saldo from produto where codprod = ?", (vcodigo,))
rs = cursor.fetchone()

print("Nome: ", rs[1],)
print("Saldo: ", rs[2],)

conn.close()
quit()


