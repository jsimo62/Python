import sqlalchemy as db

class Database:

    def __init__(self, db_name, query):
        self.db = db_name
        self.query = query


    def db_connect(self):
        engine = db.create_engine(self.db)
        results = engine.execute(self.query)
        return results

    def run_query(self):
        data = Database.db_connect(self)
        return data
