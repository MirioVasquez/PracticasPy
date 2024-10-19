import sqlite3

def show_all():
    conn = sqlite3.connect("customer.db")
    c = conn.cursor()
    c.execute('SELECT rowid, * FROM customers')

    conn.commit()

    items = c.fetchall()
    for item in items:
        print(item)

    conn.close()
    


def add_one(name,last,email):
    conn = sqlite3.connect("customer.db")
    c = conn.cursor()
    
    #print(name)
    #print(last)
    #print(email)
    
    c.execute("INSERT INTO customers VALUES (?,?,?)", (name,last,email))
    conn.commit()
    conn.close()

def val():
    valores = input("Insert a name, lastname and email: ")
    
    x,y,z = valores.split(",")
    x,y,z = x.strip(" "), y.strip(" "), z.strip(" ")
    return(x,y,z)
    
def delete_one(x):
    conn = sqlite3.connect("customer.db")
    c = conn.cursor()
    
    c.execute(f"DELETE FROM customers WHERE {x}")
    
    conn.commit()
    conn.close()