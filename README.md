# Fibonacci Calculator

## Introduction
This Flask application provides a simple web interface to calculate Fibonacci numbers. It accepts a numerical input from the user and calculates the corresponding Fibonacci number. The application is designed to be user-friendly and is built with Bootstrap for a responsive layout.

## Getting Started

### Prerequisites
Before you can run the Flask application, you need to have Python installed on your machine. You also need to install Flask if you haven't done so already. You can install Flask using the requirements file provided in this repository. To do so, run the following command in your terminal:

```bash
pip install -r requirements.txt
```

### Running the App
To run the Flask app, you need to set the environment variable `FLASK_APP` to the file that runs your application and then call `flask run` in the command line. Follow these steps:

1. Navigate to the project directory in your terminal.
2. Set the environment variable for Flask. On Unix and Mac, use:

```bash
export FLASK_APP=app.py
```

On Windows, use:

```cmd
set FLASK_APP=app.py
```

3. Run the application:

```bash
flask run
```

This will start a local server, typically on `http://127.0.0.1:5000`, where you can access the Fibonacci Calculator.

Make sure to replace `app.py` with the actual name of your Python script that initializes the Flask application.
