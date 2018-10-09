import sqlalchemy as db

engine = db.create_engine('sqlite:///census.sqlite')
connection = engine.connect()
results = connection.execute("select * from census where state='Texas' and sex='M'")
for row in results:
    print(row)

connection.close()
