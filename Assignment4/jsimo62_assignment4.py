from jsimo62_cust_class import Customer
import sqlalchemy as db
import json


engine = db.create_engine('sqlite:///customer.sqlite')
connection = engine.connect()
results = connection.execute("select * from customer")

customer = []
for row in results:
    c = Customer(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
    customer.append(c.to_json())
    name = Customer.full_name(c)
    age = Customer.age(c)
    print(name, age)

connection.close()


# print(customers)
with open('jsimo62_assignment4.json', 'w') as file:
    json.dump(customer, file)
