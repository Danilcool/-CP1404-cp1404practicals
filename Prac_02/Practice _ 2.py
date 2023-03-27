import random

print("Welcome to the Gopher Population Simulator!")

def get_death(population):
    LOWEST = 0.05
    HIGHEST = 0.25
    counter = 1 - random.uniform(LOWEST,HIGHEST)
    print(counter)
    population = population * counter
    return population

def get_life(population):
    LOWEST = 0.10
    HIGHEST = 0.20
    counter = 1 + random.uniform(LOWEST,HIGHEST)
    print(counter)
    population = population * counter
    return population

def main():
    year = 1
    population = 1000
    time_span = 10

    print(f"Starting population: {population}")
    print(f"Year {year}")
    for i in range(time_span):
        population = get_death(population)
        population = get_life(population)
        print(f"Starting population: {population}")
        print(f"Year {year}")




main()


