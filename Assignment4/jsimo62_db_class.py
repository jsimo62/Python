import sqlalchemy as db

class Database:

    def __init__(self, db_name, query):
        self.db = db_name
        self.query = query

    def db_connect(self):
        engine = db.create_engine(db_name)
        connection = engine.connect()

    def run_query(self):
        results = connection.execute(query)

    def db_disconnect():
        connection.close()
