import sqlalchemy as db

engine = db.create_engine('sqlite:///census.sqlite')
connection = engine.connect()
metadata = db.MetaData()
census = db.Table('census', metadata, autoload=True, autoload_with=engine)

print(census.columns.keys())
#return a printable version of the object
print(repr(metadata.tables['census']))
