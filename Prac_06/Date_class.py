class Date:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year


    def add_day(self,day):
        self.day += day

    def display_date(self):
        print(f"{self.day,self.month,self.year}")

Date_time = Date(17,11,2001)

Date_time.add_day(2)
print(Date_time.display_date())
