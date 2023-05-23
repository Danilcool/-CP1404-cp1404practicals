from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
menu = "q)uit, c)hoose taxi, d)rive"

def main():
    print("Let's Drive")

    user_input = ""
    picked_out_cat = None
    bill_to_date = 0
    while user_input != 'Q':
        print(menu)
        user_input = input(">>>").upper()
        if user_input == "C":
            display_cars()

            try:
                user_car_choice = int(input('Choose Taxi: '))
                picked_out_cat = taxis[user_car_choice]
                fare = picked_out_cat.get_fare()
                print(f"The current fare is: ${fare:.2f}")
            except IndexError:
                print("Invalid taxi choice.")
        elif user_input == 'D':
            if picked_out_cat is None:
                print("Please choose a taxi first.")
            else:
                try:
                    user_drive_distance = input('How far do we drive: ')
                    picked_out_cat.drive(int(user_drive_distance))
                    fare = picked_out_cat.get_fare()
                    print(f"Your {picked_out_cat.name} fare is: ${fare:.2f}")
                    bill_to_date += fare
                    print(f'Your total fare is {bill_to_date}')
                except ValueError:
                    print("Invalid distance value.")

        elif user_input == "C":
            print(f"Total trip cost: {fare}")
            print('Taxies are now')


def display_cars():
    count = 0
    for taxi in taxis:
        print(f"{count} {taxi}")
        count += 1
main()
