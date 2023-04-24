import csv
import random

# Constants
PLACES_FILE = "places.csv"

# Function to display welcome message
def display_welcome_message(name):
    print(f"Welcome {name}! This is the Place Tracker program.")

# Function to display menu options
def display_menu():
    print("Menu:")
    print("L - List all places")
    print("R - Recommend a place to visit")
    print("A - Add a place")
    print("M - Mark a place as visited")
    print("Q - Quit")

# Function to load places from CSV file
def load_places():
    places = []
    with open(PLACES_FILE, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            places.append(row)
    return places

# Function to display list of places
def display_places(places):
    max_name_length = max(len(place[0]) for place in places)
    max_country_length = max(len(place[1]) for place in places)
    print(f"{'Place':<{max_name_length}}{'Country':<{max_country_length}}{'Visited':>10}")
    for place in places:
        visited = "Yes" if place[2] == "visited" else "No"
        print(f"{place[0]:<{max_name_length}}{place[1]:<{max_country_length}}{visited:>10}")

# Function to recommend a place to visit
def recommend_place(places):

    unvisited_places = [place for place in places if place[3] == "n"]
    if len(unvisited_places) >= 1:
        random_place = random.choice(unvisited_places)
        print(f"Recommended Place: {random_place[0]} in {random_place[1]}")
    else:
        print("No unvisited places.")

# Function to add a place
def add_place(places):
    name = input("Enter place name: ")
    country = input("Enter country: ")
    priority = input("Enter priority: ")
    places.append([name, country, "unvisited", priority])
    print("Place added successfully.")

# Function to mark a place as visited
def mark_visited(places):
    unvisited_places = [place for place in places if place[3] == "n"]
    if unvisited_places:
        print("Unvisited Places:")
        display_places(unvisited_places)
        index = input("Enter index of place to mark as visited: ")
        if index.isdigit() and int(index) in range(1, len(unvisited_places) + 1):
            places[int(index) - 1][2] = "visited"
            print("Place marked as visited successfully.")
        else:
            print("Invalid index.")
    else:
        print("No unvisited places.")

# Function to save places to CSV file
def save_places(places):
    with open(PLACES_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(places)
    print("Places saved successfully.")

# Main program
def main():
    name = input("Enter your name: ")
    display_welcome_message(name)
    places = load_places()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1" or choice == 'L':
            display_places(places)
        elif choice == "2" or choice == "R":
            recommend_place(places)
        elif choice == "3" or choice == 'A':
            add_place(places)
        elif choice == "4" or choice == "M":
            mark_visited(places)
        elif choice == "5" or choice == "Q":
            save_places(places)
            print("Thank you for")
        else:
            print('Invalid Input')
main()

