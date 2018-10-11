class Dog:

    # the __init__ method initializes the object.
    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

    def remove_trick(self, trick):
        for t in self.tricks:
            if trick == t:
                self.tricks.remove(t)
                
