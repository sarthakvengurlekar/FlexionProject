# FlexionProject

A unit converter app on the cloud.

## Unit Conversion Application

This is a simple Flask application that allows users to convert units of temperature between Kelvin, Celsius, Fahrenheit, and Rankine.

The application is Dockerized and continuously deployed to an EC2 instance using Jenkins.

## Repository Structure

- **app.py** - This is the main Python script that runs the application. It defines the web routes and the conversion logic.
- **Templates** - This directory contains HTML templates used by Flask to generate the webpage. It includes:
  - **index.html** - The main page where users can input their data for conversion.
  - **error.html** - An error page which displays any error messages that occur.
  - **result.html** - The result page that displays whether the conversion result entered by the user is correct.
- **test_app.py** - This file contains tests for the application logic.
- **Dockerfile** - This file is used to create a Docker image of the application.
- **Jenkinsfile** - This file defines the Jenkins pipeline for CI/CD.
- **requirements.txt** - This file lists the Python dependencies that need to be installed.

## Installation and Running the App Locally

1. Clone the repository: `git clone https://github.com/sarthakvengurlekar/FlexionProject.git`
2. Navigate to the project directory: `cd project`
3. Install necessary dependencies: `pip install -r requirements.txt`
4. Run the application: `python app.py`
5. Access the application at `localhost:5000` in a web browser.

## Running with Docker

1. Build the Docker image: `docker build -t sarthakvengurlekar10/my_flask_app .`
2. Run the Docker container: `docker run -p 5000:5000 sarthakvengurlekar10/my_flask_app`
3. Access the application at `localhost:5000` in a web browser.

## Jenkins CI/CD Pipeline

The Jenkins pipeline is defined in the Jenkinsfile and includes the following stages:

- **Checkout** - Clones the source code from the GitHub repository.
- **Build Docker Image** - Builds the Docker image of the application.
- **Test** - Runs unit tests against the application.
- **Push Docker Image** - Pushes the Docker image to Docker Hub.
- **Deploy** - Deploys the application to an EC2 instance.

## Automating Deployment with Jenkins

The Jenkins pipeline is configured to automatically build the Docker image and deploy it to the EC2 instance whenever changes are pushed to the repository. It uses SSH to access the EC2 instance, stops and removes any previous Docker containers, pulls the latest Docker image from Docker Hub, and finally runs the new Docker container.

The application is accessible at `http://54.176.142.77:5000/` once deployed.

## Future Improvements

- **Add user authentication** - Implement a user login system to allow personalized temperature conversions.
- **Improve error handling** - Handle more error scenarios and provide more informative error messages to the user.
- **Implement a more user-friendly UI** - The current user interface is minimal and could be made more interactive and visually appealing.
- **Add more unit conversion options** - Extend the application to support other units such as length, weight, etc.
- **Enhance unit tests** - Add more comprehensive tests to ensure all application functionality is validated.