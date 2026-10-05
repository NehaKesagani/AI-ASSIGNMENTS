from feature_engg import (
    calculate_duration_score,
    calculate_stress_score,
    calculate_activity_score,
    calculate_disorder_score
)
#weights used for sleep score calculation
DURATION_WEIGHT = 0.40
STRESS_WEIGHT = 0.25
ACTIVITY_WEIGHT = 0.20
DISORDER_WEIGHT = 0.15


def calculate_sleep_score(
    sleep_duration,
    stress_level,
    activity_level,
    sleep_disorder
):
    
    duration_score = calculate_duration_score(
        sleep_duration
    )

    stress_score = calculate_stress_score(
        stress_level
    )

    activity_score = calculate_activity_score(
        activity_level
    )

    disorder_score = calculate_disorder_score(
        sleep_disorder
    )

    sleep_score = (
        DURATION_WEIGHT * duration_score +
        STRESS_WEIGHT * stress_score +
        ACTIVITY_WEIGHT * activity_score +
        DISORDER_WEIGHT * disorder_score
    )
    return sleep_score

#classify sleep score
def classify_sleep(score):
    
    if score >= 80:
        return "Excellent"

    elif score >= 65:
        return "Good"

    elif score >= 50:
        return "Moderate"

    else:
        return "Poor"