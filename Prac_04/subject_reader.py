"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    lines_list = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        lines_list.append(line)
        parts = line.split(',')  # Separate the data into its parts
        print(f'{parts[0]} is taught by {parts[1]} and has {parts[2]} students')

    input_file.close()
    return lines_list



main()