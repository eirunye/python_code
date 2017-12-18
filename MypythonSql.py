import sqlite3

# 连接到SQLite
# 数据库文件是 test.db
# 如果文件不存在，会自动创建
# conn = sqlite3.connect('test.db')
# cursor = conn.cursor()
# # 创建一个Cursor
# # cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# cursor.execute('insert into user(id,name) values(\'1\',\'Michael\')')
# #
# print(cursor.rowcount)
# cursor.close()
# conn.commit()
# conn.close()


# 查询
# conn = sqlite3.connect("test.db")
# cursor = conn.cursor()
# cursor.execute('select * from user where id =?',('1',))
#
# value = cursor.fetchall()
# print(value)
# cursor.close()
# conn.close()


import os, sqlite3

db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
	os.remove(db_file)

# 初始数据:
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute("insert into user values ('A-001', 'Adam', 95)")
cursor.execute("insert into user values ('A-002', 'Bart', 62)")
cursor.execute("insert into user values ('A-003', 'Lisa', 78)")

print(cursor.rowcount)
cursor.close()
conn.commit()
conn.close()


# conn = sqlite3.connect("test.db")
cursor = conn.cursor()
cursor.execute('select * from user where name =?','Adam')

value = cursor.fetchall()
print(value)
cursor.close()
conn.close()


# def get_score_in(low, high):
# 	pass
#
#
# assert get_score_in(80, 90)
# assert get_score_in(60, 80)
# assert get_score_in(70, 100)
#
# print('pass')

