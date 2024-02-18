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
## Installing ngrok
[ngrok download page](https://ngrok.com/download)

Follow these steps to install ngrok:

1. `wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz`
2. `tar xvzf /path/to/ngrok-v3-stable-linux-amd64.tgz`
3. `chmod +x ngrok`
4. `mv ngrok /path/to/repo/`
5. `cd /path/to/repo/`
6. `./ngrok authtoken YOUR_AUTH_TOKEN`

## Running the Application with `run.sh` Script (for lxhalle)

This project includes a convenient script named `run.sh` that automates the process of setting up and running the server on lxhalle. This script handles the creation of a virtual environment, installing dependencies, downloading and setting up ngrok, and starting the Flask application via Gunicorn with the appropriate configurations.

### Prerequisites

Before running the script, ensure you have the following installed:
- Python 3
- pip (Python package manager)
- wget (for downloading ngrok)

### Running the Script

1. **Clone the Repository**:
   First, clone the repository to your local machine and navigate to the repository folder:

   ```bash
   git clone [Repository URL]
   cd [Repository Folder]
   ```

2. **Execute the Script**:
   Run the `run.sh` script with the following command:

   ```bash
   bash run.sh
   ```

3. **Script Execution**:
   The script will perform the following actions:
   - Check for and create a virtual environment (`venv`) if it doesn't exist.
   - Activate the virtual environment and install the required dependencies from `requirements.txt`.
   - Download and set up the latest version of ngrok for Linux s390x architecture.
   - Start the Gunicorn server hosting the Flask application on `localhost:5000`.
   - Start ngrok to create a public URL tunneling to the Gunicorn server.

4. **Accessing the Application**:
   Once the script finishes execution, it will display the ngrok URL, which you can use to access the application from any web browser:
   ```
   ngrok URL: [Public ngrok URL]
   ```
   Copy and paste this URL into your browser to interact with the Flask application hosted on lxhalle.

### Logs

- Gunicorn logs are saved in `gunicorn.log`.
- ngrok logs are saved in `ngrok.log`.

You can monitor these logs for debugging and monitoring the application's behavior.
