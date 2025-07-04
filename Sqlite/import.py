import sqlite3
conn = sqlite3.connect('customer.db')       #create db 
cursor = conn.cursor()                      #cursor
cursor.execute("""CREATE TABLE IF NOT EXISTS customers(                           
               
               Name TEXT,
               Std INTEGER,
               Email TEXT
                 )""")

cursor.execute("DELETE FROM customers")

cursor.execute("INSERT INTO  customers VALUES ('vihan',2,'aryan@gmail.com')")

customers_list = [
    ('Niti',11,'abc@gmail.com'),
    ('Bhavya',3,'shah@gmail.com'),
    ('Vuri',4,"xyz@gmail.com"), 
    ]
cursor.executemany("INSERT INTO customers VALUES (?,?,?)", customers_list)
conn.commit()
cursor.execute("DELETE FROM customers WHERE rowid= 4")
cursor.execute("UPDATE customers SET Name ='Mohit' WHERE rowid = 1")
conn.commit()

cursor.execute("SELECT rowid, * FROM customers")

items = cursor.fetchall()
for item in items:
    print(items)

conn.commit()
conn.close()



