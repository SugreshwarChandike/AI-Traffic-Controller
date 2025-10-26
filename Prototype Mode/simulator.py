import random

def read_lane_data():
    lane_1 = random.randint(0, 20)
    lane_2 = random.randint(0, 20)
    emergency = random.choice([True, False])
    return lane_1, lane_2, emergency

def set_lights(decision):
    print(f"[SIMULATION] Traffic Light Decision: {decision}")