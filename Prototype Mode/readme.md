# 🔌 Prototype Folder

This folder contains the real-time, hardware-ready version of the AI Traffic Controller.

## Files
- `main.py`: Entry point for running the system on Raspberry Pi.
- `traffic_logic.py`: Core decision-making logic based on vehicle count and emergency detection.
- `hardware_input.py`: Reads data from IR sensors and emergency detectors via GPIO.
- `hardware_output.py`: Controls traffic lights (LEDs or relays) using GPIO pins.

## Purpose
Designed for direct integration with a physical prototype. This version replaces simulation with real-time sensor input and LED control.
