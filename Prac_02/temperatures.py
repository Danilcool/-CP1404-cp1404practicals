
def celsius_to_fahrenheit(temp_c):
    """Converts temperature from Celsius to Fahrenheit."""
    return (temp_c * 1.8) + 32

def fahrenheit_to_celsius(temp_f):
    """Converts temperature from Fahrenheit to Celsius."""
    return (temp_f - 32) / 1.8

def main():
    print("Do you want to convert (C)elsius or (F)ahrenheit or (Q)Quit?")
    choice = input("Enter your choice: ")
    while choice != "Q":

        if choice == "C":
            temp_c = float(input("Enter temperature in Celsius: "))
            temp_f = celsius_to_fahrenheit(temp_c)
            print(f"{temp_c}°C is {temp_f}°F")
            print("Do you want to convert (C)elsius or (F)ahrenheit or (Q)Quit?")
            choice = input("Enter your choice: ")

        elif choice == "F":
            temp_f = float(input("Enter temperature in Fahrenheit: "))
            temp_c = fahrenheit_to_celsius(temp_f)
            print(f"{temp_f}°F is {temp_c}°C")
            print("Do you want to convert (C)elsius or (F)ahrenheit or (Q)Quit?")
            choice = input("Enter your choice: ")

    if choice == "Q":
        pass
    else:
        print("Invalid choice. Please try again.")

main()

