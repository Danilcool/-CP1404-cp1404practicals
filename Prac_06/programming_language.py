
"""
Word Occurrences
Estimate: 10 minutes
Actual:   5 minutes
"""


class ProgrammingLanguage:
    def __init__(self,name,language_type,reflection,year):
        self.name = name
        self.language_type = language_type
        self.reflection = reflection
        self.year = year
        print(self.name,self.language_type,f"Reflection = {self.reflection}, " , f"First appeared in {self.year}")


