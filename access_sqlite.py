import sqlite3
conn = sqlite3.connect('enterprise.db')
curs = conn.cursor()
#drop table before practice
curs.execute('DROP TABLE zoo')

curs.execute('''CREATE TABLE zoo
    (critter VARCHAR(20) PRIMARY KEY, 
    count INT, 
    damages FLOAT)''')
# 準備SQL
ins = 'INSERT INTO zoo (critter, count, damages) VALUES(?, ?, ?)'
# insert一筆資料
curs.execute(ins, ('duck', 5, 0.0))

# 準備資料:將多組資料以tuple格式包成list
ins_data = [('bear', 2, 1000.0), ('weasel', 1, 2000.0), ('lion', 3, 4000.0)]
# insert多筆資料
curs.executemany(ins, ins_data)

# 取得資料
curs.execute('SELECT * FROM zoo ORDER BY count DESC')
rows = curs.fetchall()
print(rows)
print(type(rows))
curs.execute('''SELECT * FROM zoo 
    WHERE damages = (SELECT MAX(damages) FROM zoo)''')
rows = curs.fetchall()
print(rows)
print(type(rows[0]))
curs.close()
conn.close()
