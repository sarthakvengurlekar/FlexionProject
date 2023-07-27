# Import necessary modules from Flask
from flask import Flask, request, jsonify, render_template

# Import convert_temperature function from scipy.constants module to convert between temperature units
from scipy.constants import convert_temperature

# Create a new Flask web server from the Flask class
app = Flask(__name__)

# Function to check if a value is a number
def is_number(s):
    try:
        # Try to convert the value to a float
        float(s)
        return True
    except ValueError:
        # If a ValueError occurs it means the value can't be converted to a float, so it's not a number
        return False

# Define the main route '/'
@app.route('/')
def home():
    # Render the 'index.html' template when the main route is accessed
    return render_template('index.html')

# Define the route '/convert' which accepts POST requests
@app.route('/convert', methods=['POST'])
def convert():
    # Get the form data from the request
    data = request.form

    try:
        # Get and convert necessary values from the form data
        input_value = float(data['input_value'])
        input_unit = data['input_unit'].lower()
        target_unit = data['target_unit'].lower()
        student_response = data['student_response']
    except KeyError as e:
        # If any of the fields are missing, render an error page with the missing field
        return render_template('error.html', error=f'Missing field: {e.args[0]}')
    except ValueError:
        # If the input_value or student_response can't be converted to a float, render an error page
        return render_template('error.html', error='Invalid numerical value')

    # Check if input_value and student_response are valid numbers
    if not (is_number(input_value) and is_number(student_response)):
        return render_template('error.html', error='Invalid input, numerical values required')

    # Check if input_unit and target_unit are valid temperature units
    if input_unit not in ['kelvin', 'celsius', 'fahrenheit', 'rankine'] or target_unit not in ['kelvin', 'celsius', 'fahrenheit', 'rankine']:
        return render_template('error.html', error='Invalid unit, must be one of: kelvin, celsius, fahrenheit, rankine')

    # Calculate the correct answer using the convert_temperature function
    correct_answer = round(convert_temperature(input_value, input_unit, target_unit), 1)

    # Convert student_response to a float and round it
    student_answer = round(float(student_response), 1)

    # If the student's answer is correct, render a result page with 'Correct'
    # If not, render a result page with 'Incorrect'
    if student_answer == correct_answer:
        return render_template('result.html', result='Correct')
    else:
        return render_template('result.html', result='Incorrect')

# Check if this file is the main program and not imported as a module
if __name__ == '__main__':
    # If so, run the Flask web server
    app.run(host='0.0.0.0', port=5000)