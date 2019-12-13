import sqlite3
con=sqlite3.connect("e:\\pyprg\\mydb2.db")
cur=con.cursor()
#con.execute('''create table products(p_id integer primary key autoincrement, p_name text not null,price real,quantity integer)''');
#print("Table created")
cur.execute('''insert into products1(p_name,price) values("pepsi",150)''')
cur.execute('''insert into products1(p_name,price) values("fenta",250)''')
cur.execute('''insert into products1(p_name,price) values("coca",350)''')
print("Data inserted")
con.commit()
con.close()
