from datetime import datetime
from datetime import date
from dateutil.relativedelta import relativedelta

class Customer:

    # the __init__ method initializes the object.
    def __init__(self, id, fname, lname, dob):
        self.id = id
        self.first_name = fname
        self.last_name = lname
        self.dob = datetime.strptime(dob, '%Y-%m-%d').date()

    def age(self):
        today = date.today()
        age = relativedelta(today, self.dob)
        return age.years

    def full_name(self):
        return self.first_name + ' ' + self.last_name

    def to_json(self):
        return {'id': self.id, 'full_name': self.full_name(), 'age': self.age() }
