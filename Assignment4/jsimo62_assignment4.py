from jsimo62_cust_class import Customer
from jsimo62_db_class import Database
import json


def get_cust_data():
     db = Database("sqlite:///customer.sqlite", "select * from customer")
     cust_data = Database.run_query(db)
     return cust_data

def cust_info():
    name = Customer.full_name(c)
    age = Customer.age(c)
    address = Customer.address(c)
    return name, age, address

customer = []
for row in get_cust_data():
    c = Customer(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
    customer.append(c.to_json())
    print(cust_info())

with open('jsimo62_assignment4.json', 'w') as file:
    json.dump(customer, file)
