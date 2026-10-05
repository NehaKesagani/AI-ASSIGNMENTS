import numpy as np

def calculate_duration_score(sleep_duration):
    score = 100 - abs(sleep_duration - 8) * 25 #8 hours is considered optimal sleep duration
    return np.clip(score, 0, 100)


def calculate_stress_score(stress_level): #lower stress -> higher score
    score = ((10 - stress_level) / 9) * 100
    return np.clip(score, 0, 100)


def calculate_activity_score(activity_level): #90 mins is used as the highest reference value
    score = (activity_level / 90) * 100
    return np.clip(score, 0, 100)


def calculate_disorder_score(sleep_disorder): 
    if sleep_disorder is None:
        return 100

    if isinstance(sleep_disorder, float) and np.isnan(sleep_disorder):
        return 100

    return 0