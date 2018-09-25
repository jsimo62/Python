import sqlalchemy as db

engine = db.create_engine('sqlite:///census.sqlite')
connection = engine.connect()
metadata = db.MetaData()
census = db.Table('census', metadata, autoload=True, autoload_with=engine)
state_fact = db.Table('state_fact', metadata, autoload=True, autoload_with=engine)

query = db.select([census.columns.pop2008, state_fact.columns.abbreviation])
result = connection.execute(query).fetchall()

print(result[:10])
