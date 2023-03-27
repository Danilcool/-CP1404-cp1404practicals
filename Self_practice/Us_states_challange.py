

file = open("US-States.txt")

total = 0
states = 0
low_state_population = 1000000
high_state_population = 0

for line in file:
    data = line.split(",")
    state = data[0]
    Id = data[1]
    population = int(data[2])

    total += population
    states += 1

    if population > high_state_population:
        high_state_population = population
    else:
        population < low_state_population
        low_state_population = population

average = total / states

print(total,states,high_state_population, low_state_population,)