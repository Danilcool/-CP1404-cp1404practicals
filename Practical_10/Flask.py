from flask import Flask
from quoters import Quote

app = Flask(__name__)

# Temperature conversion function
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Route for Celsius to Fahrenheit conversion
@app.route('/convert/<celsius>')
def convert_celsius_to_fahrenheit(celsius):
    try:
        celsius = float(celsius)
        fahrenheit = celsius_to_fahrenheit(celsius)
        return f"The temperature of {celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit."
    except ValueError:
        return "Invalid input. Please enter a valid temperature in Celsius."

def quote():
    return Quote.print()
if __name__ == '__main__':
    app.run()