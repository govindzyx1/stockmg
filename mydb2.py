import sqlite3
con=sqlite3.connect("e:\\pyprg\\mydb2.db")
#cur=con.cursor()
con.execute('''create table if not exists products1(p_id integer primary key autoincrement, p_name text not null,price real,quantity integer)''')
print("Table created")
con.close()
