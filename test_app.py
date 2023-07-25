import pytest
from flask import Flask, url_for
from flask_testing import TestCase
from app import app, convert  

class TestApp(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    # Test 1: Check home page
    def test_home_page(self):
        response = self.client.get(url_for('home'))
        self.assert200(response)

    # Test 2: Test correct conversion from Celsius to Fahrenheit
    def test_correct_celsius_to_fahrenheit(self):
        response = self.client.post(
            url_for('convert'),
            data={
                'input_value': '100',
                'input_unit': 'celsius',
                'target_unit': 'fahrenheit',
                'student_response': '212'
            }
        )
        assert 'Correct' in response.data.decode('utf-8')

    # Test 3: Test incorrect conversion from Celsius to Fahrenheit
    def test_incorrect_celsius_to_fahrenheit(self):
        response = self.client.post(
            url_for('convert'),
            data={
                'input_value': '100',
                'input_unit': 'celsius',
                'target_unit': 'fahrenheit',
                'student_response': '213'
            }
        )
        assert 'Incorrect' in response.data.decode('utf-8')

    # Test 4: Test invalid temperature unit
    def test_invalid_unit(self):
        response = self.client.post(
            url_for('convert'),
            data={
                'input_value': '100',
                'input_unit': 'celcius',  # Misspelled unit
                'target_unit': 'fahrenheit',
                'student_response': '212'
            }
        )
        assert 'Invalid unit, must be one of: kelvin, celsius, fahrenheit, rankine' in response.data.decode('utf-8')

    # Test 5: Test missing field
    def test_missing_field(self):
        response = self.client.post(
            url_for('convert'),
            data={
                'input_value': '100',
                # Missing 'input_unit' field
                'target_unit': 'fahrenheit',
                'student_response': '212'
            }
        )
        assert 'Missing field' in response.data.decode('utf-8')

    # Test 6: Test invalid numerical value for temperature
    def test_invalid_temperature(self):
        response = self.client.post(
            url_for('convert'),
            data={
                'input_value': 'abc',  # Not a number
                'input_unit': 'celsius',
                'target_unit': 'fahrenheit',
                'student_response': '212'
            }
        )
        assert 'Invalid numerical value' in response.data.decode('utf-8')

    # Test 7: Test invalid numerical value for student response
    def test_invalid_student_response(self):
        response = self.client.post(
            url_for('convert'),
            data={
                'input_value': '100',
                'input_unit': 'celsius',
                'target_unit': 'fahrenheit',
                'student_response': 'abc'  # Not a number
            }
        )
        assert 'Invalid input, numerical values required' in response.data.decode('utf-8')

    # Test 8: Test correct conversion from Fahrenheit to Celsius
    def test_correct_fahrenheit_to_celsius(self):
        response = self.client.post(
            url_for('convert'),
            data={
                'input_value': '212',
                'input_unit': 'fahrenheit',
                'target_unit': 'celsius',
                'student_response': '100'
            }
        )
        assert 'Correct' in response.data.decode('utf-8')


if __name__ == '__main__':
    pytest.main()
