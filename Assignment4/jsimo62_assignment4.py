from jsimo62_cust_class import Customer
from jsimo62_db_class import Database
import json


cust_db = "sqlite:///customer.sqlite"
cust_query = "SELECT * FROM customer"

def get_cust_data():
     db = Database(cust_db, cust_query + " ORDER BY last_name ASC")
     cust_data = Database.run_query(db)
     return cust_data

def get_cust_data_by_state():
    if c.state == 'GA':
        print(Customer.full_name(c), "|", Customer.age(c), "|", Customer.location(c))
    return

customer = []
for row in get_cust_data():
    c = Customer(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
    customer.append(c.to_json())
    get_cust_data_by_state()

with open('jsimo62_assignment4.json', 'w') as file:
    json.dump(customer, file)
