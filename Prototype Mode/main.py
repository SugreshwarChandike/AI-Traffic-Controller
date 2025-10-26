from traffic_logic import decide_light

# Toggle this when hardware arrives
USE_HARDWARE = False

if USE_HARDWARE:
    from hardware_input import read_lane_data
    from hardware_output import set_lights
else:
    from simulator import read_lane_data, set_lights

import time

def run_traffic_controller():
    while True:
        lane_1, lane_2, emergency = read_lane_data()
        decision = decide_light(lane_1, lane_2, emergency)
        print(f"Lane 1: {lane_1}, Lane 2: {lane_2}, Emergency: {emergency}")
        set_lights(decision)
        time.sleep(5)

if __name__ == "__main__":
    run_traffic_controller()
