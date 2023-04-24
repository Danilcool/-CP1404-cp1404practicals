"""
Word Occurrences
Estimate: 10 minutes
Actual:   10 minutes
"""

from guitar import Guitar

guitar = Guitar(name="Gibson L-5 CES", year=1923,cost = "100$")
guitar2 = Guitar(name="Another Guitar", year=2014,cost = "100$")

print(f"""Gibson L-5 CES get_age() - Expected 100. Got {guitar.get_age()}
Another Guitar get_age() - Expected 9. Got {guitar2.get_age()}
Gibson L-5 CES is_vintage() - Expected True. Got {guitar.is_vintage()}
Another Guitar is_vintage() - Expected False. Got {guitar2.is_vintage()}""")


