# 同关系型数据库进行交互

import sqlite3
db = sqlite3.connect('database.db')

c = db.cursor()
#c.execute('create table portfolio (symbol text,shares integer,price real)')
#db.commit()


stocks = [('GOOG',100,490.1),('AAPL',50,545.75),('FB',150,7.45)]

c.executemany('insert into portfolio values (?,?,?)',stocks)
db.commit()



min_price =8.0
for row in db.execute('select * from portfolio where price > ?',(min_price,)):
    print(row)