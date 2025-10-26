import RPi.GPIO as GPIO

def setup_outputs():
    GPIO.setmode(GPIO.BCM)

    # 🔴 Lane 1 Red LED — Replace 5 with the GPIO pin you connected
    GPIO.setup(5, GPIO.OUT)   # Lane 1 Red LED (GPIO 5)

    # 🟢 Lane 1 Green LED — Replace 6 with the GPIO pin you connected
    GPIO.setup(6, GPIO.OUT)   # Lane 1 Green LED (GPIO 6)

    # 🔴 Lane 2 Red LED — Replace 13 with the GPIO pin you connected
    GPIO.setup(13, GPIO.OUT)  # Lane 2 Red LED (GPIO 13)

    # 🟢 Lane 2 Green LED — Replace 19 with the GPIO pin you connected
    GPIO.setup(19, GPIO.OUT)  # Lane 2 Green LED (GPIO 19)

def set_lights(decision):
    if decision == "Green for Lane 1":
        GPIO.output(6, GPIO.HIGH)   # Lane 1 Green ON
        GPIO.output(5, GPIO.LOW)    # Lane 1 Red OFF
        GPIO.output(13, GPIO.HIGH)  # Lane 2 Red ON
        GPIO.output(19, GPIO.LOW)   # Lane 2 Green OFF

    elif decision == "Green for Lane 2":
        GPIO.output(6, GPIO.LOW)    # Lane 1 Green OFF
        GPIO.output(5, GPIO.HIGH)   # Lane 1 Red ON
        GPIO.output(13, GPIO.LOW)   # Lane 2 Red OFF
        GPIO.output(19, GPIO.HIGH)  # Lane 2 Green ON

    elif decision == "Emergency Priority":
        GPIO.output(6, GPIO.HIGH)   # Lane 1 Green ON
        GPIO.output(5, GPIO.LOW)    # Lane 1 Red OFF
        GPIO.output(13, GPIO.LOW)   # Lane 2 Red OFF
        GPIO.output(19, GPIO.HIGH)  # Lane 2 Green ON

    else:  # Alternate Lanes
        GPIO.output(6, GPIO.HIGH)   # Lane 1 Green ON
        GPIO.output(19, GPIO.HIGH)  # Lane 2 Green ON
        GPIO.output(5, GPIO.LOW)    # Lane 1 Red OFF
        GPIO.output(13, GPIO.LOW)   # Lane 2 Red OFF