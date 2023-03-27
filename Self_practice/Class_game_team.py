"""
kids_in_class = []


with open('class.txt') as f:
   for l in f:
       kids_in_class.append(l.strip().split("\t"))

teams_split = int(input("how many teams do you want"))

team_split_number = len(kids_in_class) / teams_split

team = 1
for i in range(int(teams_split)):
    print(f'team {team}')
    team += 1
    for i in range(int(team_split_number)):
        print(kids_in_class[i])



print(team_split_number)
"""

kids_in_class = []

with open('class.txt') as f:
   for l in f:
       kids_in_class.append(l.strip())

teams_split = int(input("How many teams do you want? "))
team_split_number = len(kids_in_class) // teams_split

team = 1
for i in range(teams_split):
    print(f'Team {team}:')
    team += 1
    for j in range(i * team_split_number, (i + 1) * team_split_number):
        print(kids_in_class[j])
    print()

print(team_split_number)