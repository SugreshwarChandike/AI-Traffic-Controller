import RPi.GPIO as GPIO

def setup_inputs():
    GPIO.setmode(GPIO.BCM)

    # 🟢 Lane 1 IR Sensor — Replace 17 with the GPIO pin you connected
    GPIO.setup(17, GPIO.IN)  # Lane 1 IR Sensor (GPIO 17)

    # 🟢 Lane 2 IR Sensor — Replace 27 with the GPIO pin you connected
    GPIO.setup(27, GPIO.IN)  # Lane 2 IR Sensor (GPIO 27)

    # 🟢 Emergency Sensor — Replace 22 with the GPIO pin you connected
    GPIO.setup(22, GPIO.IN)  # Emergency Sensor (GPIO 22)

def read_lane_data():
    # Make sure these match the pins used in setup_inputs()
    lane_1 = GPIO.input(17)      # Lane 1 IR Sensor
    lane_2 = GPIO.input(27)      # Lane 2 IR Sensor
    emergency = GPIO.input(22)   # Emergency Sensor
    return lane_1, lane_2, emergency