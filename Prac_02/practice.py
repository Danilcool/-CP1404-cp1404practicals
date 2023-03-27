# Define a function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Open the input file for reading and the output file for appending
with open("temps_input.txt", "r") as input_file, open("temps_output.txt", "a") as output_file:
    # Loop over each line in the input file
    for line in input_file:
        # Convert the temperature from Fahrenheit to Celsius
        temperature = fahrenheit_to_celsius(int(line))
        # Write the temperature to the output file followed by a newline character
        output_file.write(str(temperature) + "\n")



