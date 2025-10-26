import time
import logging
import RPi.GPIO as GPIO
from traffic_logic import decide_light

# 🔧 Toggle between simulation and hardware mode
USE_HARDWARE = True

# 📥 Import input/output modules based on mode
if USE_HARDWARE:
    from hardware_input import setup_inputs, read_lane_data
    from hardware_output import setup_outputs, set_lights
else:
    from simulator import read_lane_data, set_lights

# 📝 Enable logging
logging.basicConfig(filename='traffic_log.txt', level=logging.INFO)

# 🚦 Main traffic controller loop
def run_traffic_controller():
    while True:
        lane_1, lane_2, emergency = read_lane_data()
        decision = decide_light(lane_1, lane_2, emergency)

        print(f"Lane 1: {lane_1}, Lane 2: {lane_2}, Emergency: {emergency}")
        print(f"Decision: {decision}")
        logging.info(f"Lane1: {lane_1}, Lane2: {lane_2}, Emergency: {emergency}, Decision: {decision}")

        set_lights(decision)
        time.sleep(5)

# 🚀 Entry point
if __name__ == "__main__":
    try:
        if USE_HARDWARE:
            setup_inputs()
            setup_outputs()
        run_traffic_controller()
    except KeyboardInterrupt:
        print("\nShutting down safely...")
        GPIO.cleanup()