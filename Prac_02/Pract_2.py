import random

def get_death(population):
    death_rate = random.uniform(0.05, 0.25)
    population *= 1 - death_rate
    return population

def get_life(population):
    growth_rate = random.uniform(0.10, 0.20)
    population *= 1 + growth_rate
    return population

def simulate_population(years, initial_population):
    print("Welcome to the Gopher Population Simulator!")
    print(f"Starting population: {initial_population}")
    for year in range(1, years+1):
        population = get_death(initial_population)
        population = get_life(population)
        print(f"Year {year}")
        print(f"Population: {population:.0f}")
        initial_population = population

simulate_population(years=10,initial_population=1000)