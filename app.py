from flask import Flask, request, jsonify
from scipy.constants import convert_temperature
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    data = request.form

    try:
        input_value = float(data['input_value'])
        input_unit = data['input_unit'].lower()
        target_unit = data['target_unit'].lower()
        student_response = data['student_response']
    except KeyError as e:
        return render_template('error.html', error=f'Missing field: {e.args[0]}')
    except ValueError:
        return render_template('error.html', error='Invalid numerical value')

    if not (is_number(input_value) and is_number(student_response)):
        return render_template('error.html', error='Invalid input, numerical values required')

    if input_unit not in ['kelvin', 'celsius', 'fahrenheit', 'rankine'] or target_unit not in ['kelvin', 'celsius', 'fahrenheit', 'rankine']:
        return render_template('error.html', error='Invalid unit, must be one of: kelvin, celsius, fahrenheit, rankine')

    correct_answer = round(convert_temperature(input_value, input_unit, target_unit), 1)
    student_answer = round(float(student_response), 1)

    if student_answer == correct_answer:
        return render_template('result.html', result='Correct')
    else:
        return render_template('result.html', result='Incorrect')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)