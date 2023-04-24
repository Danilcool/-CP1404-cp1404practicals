from guitar import Guitar


"""
Word Occurrences
Estimate: 20 minutes
Actual:   25 minutes
"""





def main():
    guitars_list = []
    print('Guitars')
    guitar_name = input('Name:')

    while guitar_name != '':
        try:
            guitar_year = int(input('Year:'))
            guitar_cost = int(input('Cost:'))
            print(f"{guitar_name} ({guitar_year}) : ${guitar_cost} added.")
            guitars_list.append(Guitar(guitar_name, guitar_year, guitar_cost))
            guitar_name = input('Name:')

        except ValueError:
            print('Year and Cost must be numerical')

    for i, guitar in enumerate(guitars_list, 0):
        if guitar.is_vintage() == True:
            vintage_string = "(Vintage)"
        else:
            vintage_string = ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")

main()