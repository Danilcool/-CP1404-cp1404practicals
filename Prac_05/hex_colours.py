"""
Word Occurrences
Estimate: 10 minutes
Actual:   9 minutes
"""

HEX_COLORS = {
    "Red": "#FF0000",  # Red
    "Green": "#00FF00",  # Green
    "Blue": "#0000FF",  # Blue
    "Yellow": "#FFFF00",  # Yellow
    "Magenta": "#FF00FF",  # Magenta
    "Cyan": "#00FFFF",  # Cyan
    "Orange": "#FFA500",  # Orange
    "Purple": "#800080",  # Purple
    "Teal": "#008080",  # Teal
    "Brown": "#A52A2A",  # Brown
}

while True:
    user_input = input('What colour would you like to look up:').capitalize()

    if user_input not in HEX_COLORS:
        if user_input == "":
            print("End of Program")
            break
        print('Invalid Name')

    selected_color = HEX_COLORS[user_input]
    print(f'The color code for {user_input} is {selected_color}')
    user_input = input('What colour would you like to look up:').capitalize()
