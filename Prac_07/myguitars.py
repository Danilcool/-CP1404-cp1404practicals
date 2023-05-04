import csv


class Guitar:
    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost}"

    def __lt__(self, other):
        return self.year < other.year


def read_guitars(filename):
    guitars = []
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for line in reader:
            name, year, cost = line
            guitar = Guitar(name, int(year), float(cost))
            guitars.append(guitar)
    return guitars


def write_guitars(filename, guitars):
    with open(filename, "w", newline='') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


def get_guitar():
    name = input("Enter guitar name: ")
    year = int(input("Enter guitar year: "))
    cost = float(input("Enter guitar cost: "))
    return Guitar(name, year, cost)


filename = "guitars.csv"

guitars = read_guitars(filename)

for guitar in guitars:
    print(guitar)

new_guitar = get_guitar()
guitars.append(new_guitar)

write_guitars(filename, guitars)
