import sqlite3

# 连接到 SQLite 数据库
db_connection = sqlite3.connect("db.sqlite3")
cursor = db_connection.cursor()

# 查询所有表名
cursor.execute("SELECT name FROM sqlite_sequence")
tables = cursor.fetchall()

# 打印所有表名
for table in tables:
    print(table[0])

# 关闭数据库连接
cursor.close()
db_connection.close()