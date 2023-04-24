
"""
Word Occurrences
Estimate: 10 minutes
Actual:   5 minutes
"""
class Guitar:

    def __init__(self,name="",year=0,cost=0):
        self.name = name
        self.year = year
        self.cost = cost


    def get_age(self):
        age = 2023 - self.year
        return age

    def is_vintage(self):
        age = self.get_age()
        if age >= 50:
            return True
        else:
            return False
