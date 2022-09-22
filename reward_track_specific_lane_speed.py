def reward_function(params):

    center_variance = params["distance_from_center"] / params["track_width"]
    #racing line
    range_left_1 = list(range(23,39))
    range_left_2 = list(range(66,71))
    range_left_3 = list(range(80,88))
    range_left_4 = list(range(105,110))
    left_lane = range_left_1 + range_left_2 + range_left_3 + range_left_4

    range_center_1 = list(range(1,22))
    range_center_2 = list(range(40,51))
    range_center_3 = list(range(58,65))
    range_center_4 = list(range(72,79))
    range_center_5 = list(range(89,104))
    range_center_6 = list(range(111,118))
    center_lane = range_center_1 + range_center_2 + range_center_3 + range_center_4 + range_center_5 + range_center_6


    range_right_1 = list(range(52,57))
    right_lane = range_right_1

    #Speed
    range_fast_1 = list(range(1,21))
    range_fast_2 = list(range(43,50))
    range_fast_3 = list(range(55,64))
    range_fast_4 = list(range(70,79))
    range_fast_5 = list(range(89,104))
    range_fast_6 = list(range(111,118))
    fast = range_fast_1 + range_fast_2 + range_fast_3 + range_fast_4 + range_fast_5 + range_fast_6

    slow = list(range(1,118))
    for i in fast:
        del slow[slow.index(i)]

    reward = 21

    if params["all_wheels_on_track"]:
        reward += 10
    else:
        reward -= 10

    if params["closest_waypoints"][1] in left_lane and params["is_left_of_center"]:
        reward += 10
    elif params["closest_waypoints"][1] in right_lane and not params["is_left_of_center"]:
        reward += 10
    elif params["closest_waypoints"][1] in center_lane and center_variance < 0.4:
        reward += 10
    else:
        reward -= 10
    if params["closest_waypoints"][1] in fast:
        if params["speed"] == 2 :
            reward += 10
        else:
            reward -= 10
    elif params["closest_waypoints"][1] in slow:
        if params["speed"] == 1 :
            reward += 10
        else:
            reward -= 10


    return float(reward)
