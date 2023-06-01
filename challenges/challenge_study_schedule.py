def study_schedule(permanence_period, target_time):
    count = 0
    for index in range(len(permanence_period)):
        if (
            not type(permanence_period[index][0]) is int
            or not type(permanence_period[index][1]) is int
        ):
            return None
        if target_time in range(
            permanence_period[index][0],
            permanence_period[index][1] + 1,
        ):
            count += 1
    if count:
        return count
