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

Follow these steps to install ngrok:

1. **Download ngrok**

   Visit the [ngrok download page](https://ngrok.com/download) and download the zip file for your operating system.

2. **Unzip the file**

   Unzip the downloaded file to extract the ngrok executable. On Unix systems, you can use the `unzip` command:

   ```bash
   unzip /path/to/ngrok.zip
   ```

   Replace `/path/to/ngrok.zip` with the path where you downloaded the ngrok zip file.

3. **Make ngrok executable**

   On Unix systems, you may need to make the ngrok file executable:

   ```bash
   chmod +x /path/to/ngrok
   ```

   Replace `/path/to/ngrok` with the path where you unzipped the ngrok executable.

4. **Move ngrok to your PATH**

   To be able to run ngrok from any directory, move the ngrok executable to a directory that's on your system's PATH. On Unix systems, you can use the `mv` command:

   ```bash
   mv /path/to/ngrok /usr/local/bin
   ```

   Replace `/path/to/ngrok` with the path where you unzipped the ngrok executable.

5. **Connect your account**

   Run the following command to add your ngrok authtoken (you can find this on your ngrok dashboard after you sign up and log in):

   ```bash
   ngrok authtoken YOUR_AUTH_TOKEN
   ```

   Replace `YOUR_AUTH_TOKEN` with your actual ngrok authtoken.

6. **Test the installation**

   You can test that ngrok is working by starting a tunnel:

   ```bash
   ngrok http 80
   ```

   If ngrok is installed correctly, you should see a ngrok logging interface in your terminal.

Remember to replace `/path/to/ngrok` with the actual path to the ngrok executable on your system.

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
