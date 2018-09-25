import sqlalchemy as db

engine = db.create_engine('sqlite:///census.sqlite')
connection = engine.connect()
metadata = db.MetaData()
census = db.Table('census', metadata, autoload=True, autoload_with=engine)

# Equivalent to:
# SELECT * FROM census WHERE sex = F
#query = db.select([census]).where(census.columns.sex == 'F')

# Equivalent to:
# SELECT state, sex FROM census WHERE state IN (Texas, New York)
query = db.select([census.columns.state, census.columns.sex]).where(census.columns.state.in_(['Texas', 'New York']))

proxy = connection.execute(query)
print(proxy)

result = proxy.fetchall()

print(result[:10])
