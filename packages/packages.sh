#!/bin/bash

VENV_NAME="metrics_env"

if [ ! -d "$VENV_NAME" ]; then
  echo " Creating virtual environment..."
  python3 -m venv "$VENV_NAME"
fi

# Activate the venv
source "$VENV_NAME/bin/activate"

echo " Installing packages..."
pip install --upgrade pip
pip install psutil matplotlib prettytable numpy

echo "Installation complete."

