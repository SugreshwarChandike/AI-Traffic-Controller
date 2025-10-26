def decide_light(lane_1, lane_2, emergency):
    if emergency:
        return "Emergency Priority"
    elif lane_1 > lane_2:
        return "Green for Lane 1"
    elif lane_2 > lane_1:
        return "Green for Lane 2"
    else:
        return "Alternate Lanes"