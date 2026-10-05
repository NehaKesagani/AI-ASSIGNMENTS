from sleep_score import (
    calculate_sleep_score,
    classify_sleep
)

from agent_explanation import (
    generate_reason,
    generate_recommendation
)
#analysis of one person's sleep condition using the intelligent agent
def analyze_person(
    age,
    sleep_duration,
    stress_level,
    activity_level,
    sleep_disorder
):

    sleep_score = calculate_sleep_score(
        sleep_duration,
        stress_level,
        activity_level,
        sleep_disorder
    )

    sleep_category = classify_sleep(
        sleep_score
    )

    reason = generate_reason(
        sleep_duration,
        stress_level,
        activity_level,
        sleep_disorder
    )

    recommendation = generate_recommendation(
        sleep_duration,
        stress_level,
        activity_level,
        sleep_disorder
    )

    result = {
        "Age": age,
        "Sleep Score": round(sleep_score, 2),
        "Sleep Category": sleep_category,
        "Reason": reason,
        "Recommendation": recommendation
    }

    return result