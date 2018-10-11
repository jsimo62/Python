from jdavi48_cust_class import Customer
import sqlalchemy as db
import json

engine = db.create_engine('sqlite:///customer.sqlite')
connection = engine.connect()
results = connection.execute("select * from customer")

customers = []
for row in results:
    #print(row)
    c = Customer(row[0], row[1], row[2], row[3])
    customers.append(c.to_json())

connection.close()

# print(customers)
with open('jdavi48_assignment4.json', 'w') as file:
    json.dump(customers, file)
