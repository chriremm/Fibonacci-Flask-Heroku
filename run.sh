#!/bin/bash

# Pfad zur virtuellen Umgebung und App
VENV_PATH="venv/bin/activate"
APP_PATH="venv/bin/gunicorn"
APP_MODULE="app:app"

# Check if venv exists
if [ ! -d "venv" ]; then
  echo "venv not found, creating venv..."
  python -m venv venv
fi

echo "Activating venv and installing requirements..."

# Aktivieren der virtuellen Umgebung
source $VENV_PATH

# Install requirements
pip install -r requirements.txt

# Check if ngrok not exists
if [ ! -f "ngrok" ]; then
  # ngrok exists
  echo "Downloading ngrok..."
  # Download ngrok tar
  wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz

  echo "Unpacking ngrok..."

  # Entpacken von ngrok
  tar -xzf ngrok-v3-stable-linux-s390x.tgz
fi

chmod +x ngrok

echo "Starting gunicorn..."

# Starten von Gunicorn im Hintergrund
nohup nice -n 10 $APP_PATH -w 4 $APP_MODULE --bind 127.0.0.1:5000 > gunicorn.log 2>&1 &

# Warten, um sicherzustellen, dass Gunicorn hochgefahren ist
sleep 5

echo "Starting ngrok..."

# Starten von ngrok im Hintergrund und Abrufen der öffentlichen URL
nohup ./ngrok http 5000 > ngrok.log 2>&1 &
sleep 5 # Warten, damit ngrok Zeit hat, sich zu verbinden

# Abrufen der ngrok URL
NGROK_URL=$(curl --silent http://127.0.0.1:4040/api/tunnels | grep -o '"public_url":"[^"]*' | grep -o 'http[^"]*')

# Ausgabe der ngrok URL
echo "ngrok URL: $NGROK_URL"

# Skript beenden und Prozesse im Hintergrund laufen lassen
exit 0