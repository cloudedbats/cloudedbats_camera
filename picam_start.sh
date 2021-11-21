#!/bin/bash

# Activate the virtual environment (venv) for Python.
cd /home/pi/cloudedbats_camera
source venv/bin/activate

# Defined environment variables.
# export PICAM_HOST=0.0.0.0
# export PICAM_PORT=8082
# export PICAM_LOG_LEVEL=info

# Launch the camera.
python3 picam_start.py
