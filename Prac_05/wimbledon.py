"""
Word Occurrences
Estimate: 25 minutes
Actual:   20 minutes
"""

player_dict = {}
country_list = []
COUNT_RAISE = 1


def main():
    with open("wimbledon.csv", "r", encoding="utf-8-sig") as in_file:
        for line in in_file.readlines():
            line_components = line.split(',')
            find_player(line_components)
            find_country(line_components)

    final_display()


def find_player(line_components):
    player = line_components[2]
    if player not in player_dict:
        player_dict[player] = COUNT_RAISE
    else:
        player_dict[player] += COUNT_RAISE


def find_country(line_components):
    country = line_components[1]

    if country not in country_list:
        country_list.append(country)


def final_display():
    player_dict.pop("Champion")

    for player in player_dict:
        print(player, player_dict[player])

    country_list.pop(0)
    print(f"These {len(country_list)} countries have won Wimbledon: ")
    for country in sorted(country_list):
        print(country, end=', ')


main()
