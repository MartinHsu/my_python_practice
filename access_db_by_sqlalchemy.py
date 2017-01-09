# create_engine連結參考 http://docs.sqlalchemy.org/en/latest/core/engines.html
## Unix/Mac - 4 initial slashes in total
# engine = create_engine('sqlite:////absolute/path/to/foo.db')
## Windows
# engine = create_engine('sqlite:///C:\\path\\to\\foo.db')
## Windows alternative using raw string
# engine = create_engine(r'sqlite:///C:\path\to\foo.db')

# 使用SQLAlchemy的引擎層來做DB存取
import sqlalchemy as sa
conn = sa.create_engine('sqlite://') #連結為空，表示SQLite :memory: database
conn.execute('''CREATE TABLE zoo
    (critter VARCHAR(20) PRIMARY KEY,
    count INT,
    damages FLOAT)''')
ins = 'INSERT INTO zoo (critter, count, damages) VALUES (?, ?, ?)'
conn.execute(ins, 'duck', 10, 0.0)
conn.execute(ins, 'bear', 2, 1000.0)
conn.execute(ins, 'weasel', 1, 2000.0)
rows = conn.execute('SELECT * FROM zoo')
print(rows)

for row in rows:
	print(row)

# 使用SQL Expression Language來做DB存取
conn2 = sa.create_engine('sqlite://') 
meta = sa.MetaData()
zoo2 = sa.Table('zoo2', meta,
	sa.Column('critter', sa.String, primary_key=True),
	sa.Column('count', sa.Integer),
	sa.Column('damages', sa.Float)
	)
meta.create_all(conn2)
conn2.execute(zoo2.insert(('bear', 2, 1000.0)))
conn2.execute(zoo2.insert(('weasel', 1, 2000.0)))
conn2.execute(zoo2.insert(('duck', 10, 0.0)))

result = conn2.execute(zoo2.select())
rows2 = result.fetchall()
print(rows2)

# 使用ORM來做DB存取
from sqlalchemy.ext.declarative import declarative_base
conn3 = sa.create_engine('sqlite:///zoo.db')
Base = declarative_base()

class Zoo(Base):
    __tablename__='zoo'
    critter = sa.Column('critter', sa.String, primary_key=True)
    count = sa.Column('count', sa.Integer)
    damages = sa.Column('damages', sa.Float)

    def __init__(self, critter, count, damages):
        self.critter = critter
        self.count = count
        self.damages = damages

    def __repr__(self):
        return "<Zoo({}, {}, {})>".format(self.critter, self.count, self.damages)


Base.metadata.create_all(conn3) #建立資料庫與資料表
first = Zoo('duck', 10, 0.0)
second = Zoo('bear', 2, 1000.0)
third = Zoo('weasel', 1, 2000.0)
print(first)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=conn3)
session = Session()

session.add(first)
session.add_all([second, third])

session.commit()




    