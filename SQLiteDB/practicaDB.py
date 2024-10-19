import sqlite3

#conn = sqlite3.connect(':memory:') #para guardar informacion temporal que despues se va a eliminar#
#conectando a la base de datos
conn = sqlite3.connect('customer.db')

#creando un "cursor"
c = conn.cursor()

#haciendo un commit multiple
#many_customers = [
#                    ('Wes', 'Brown', 'wes@brown.com'),
#                    ('Steph', 'Kuewa', 'steph@kuewa.com'),
#                    ('Dan', 'Pas', 'dan@pas.com'),
#                ]

#creando una tabla
#c.execute(""""CREATE TABLE customers (
#        first_name text,
#        last_name text,
#        email text
#    )""")

#many = [
#    ("Maria", "Pinto", "mapi@gmai.com"),
#    ("Carlos", "Rodriguez", "caro@gmail.com"),
#    ("Alberto", "Lepage", "alpes@gmai.com"),
#    ("Mirian", "Sotelo", "miso@gmail.com"),
#    ("Brayan", "Lazaro", "labra@gmail.com"),
#]

#c.executemany('INSERT INTO customers VALUES (?,?,?)', many)

#c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)

#print("Command executed succesfully...")

#c.execute("SELECT * FROM customers WHERE email LIKE '%codemy.com'")
#Como usar el where y like

#update records
#c.execute("""UPDATE customers SET first_name = 'Wes'
#          WHERE rowid = '4'
#          """)
#c.execute("SELECT rowid, * FROM customers")

#Delete Record
#c.execute("DELETE from customers WHERE first_name = 'Dan'")
#c.execute("SELECT rowid, * FROM customers")


#c.fetchone()[0] Fetch the first value from the db
#c.fetchmany(3) Fetch how many values we want
#c.fetchall()fetch everything

#ordenando la tabla
#c.execute("SELECT rowid, * FROM customers ORDER BY first_name DESC")

#AND & OR
#c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'Br%' AND rowid <= 3")

#Limit
#c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC LIMIT 4")

#Delete a Table
#c.execute("DROP TABLE customers")

conn.commit()


items = c.fetchall()

#print("NAME " + "\t\tEMAIL")
#print("-------" + "\t\t---------")
for item in items:
    print(item)

#commit el comando
conn.commit()

#cerrar la coneccion
conn.close()

# DATATYPE: 
# NULL
# INTEGER
# REAL
# TEXT
# BLOB