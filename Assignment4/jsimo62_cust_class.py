from datetime import datetime as datetime
from datetime import date
from dateutil.relativedelta import relativedelta

class Customer:

    def __init__(self, cust_id, first, last, bday, city, state, zip):
        self.cust_id = cust_id
        self.first = first
        self.last = last
        self.bday = datetime.strptime(bday, '%Y-%m-%d').date()
        self.city = city
        self.state = state
        self.zip = zip

    def full_name(self):
        return self.first + " " + self.last

    def age(self):
        today = date.today()
        age = relativedelta(today, self.bday)
        return age.years

    def address(self):
        return self.full_name() + " | " + self.city + ", " + self.state + " " + self.zip

    def to_json(self):
        return {'id': self.cust_id,
                'full_name': self.full_name(),
                'age': self.age(),
                'contact_info': self.address()}
