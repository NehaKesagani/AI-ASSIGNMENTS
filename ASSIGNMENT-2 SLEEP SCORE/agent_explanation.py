import pandas as pd
#reasoning by considering the features
def generate_reason(
    sleep_duration,
    stress_level,
    activity_level,
    sleep_disorder
):
    reasons = []

    if sleep_duration >= 7:
        reasons.append("adequate sleep duration")
    else:
        reasons.append("low sleep duration")

    if stress_level <= 4:
        reasons.append("low stress")
    elif stress_level >= 7:
        reasons.append("high stress")
    else:
        reasons.append("moderate stress")

    if activity_level >= 60:
        reasons.append("good physical activity")
    else:
        reasons.append("no proper physical activity")

    if pd.isna(sleep_disorder):
        reasons.append("no sleep disorder recorded")
    else:
        reasons.append(
            f"reported {sleep_disorder}"
        )

    return ", ".join(reasons)

#recommendations based on the features
def generate_recommendation(
    sleep_duration,
    stress_level,
    activity_level,
    sleep_disorder
):

    recommendations = []

    if sleep_duration < 7:
        recommendations.append(
            "Try to increase your sleep duration."
        )

    if stress_level >= 7:
        recommendations.append(
            "Try to reduce stress before bedtime."
        )

    if activity_level < 60:
        recommendations.append(
            "Consider increasing your physical activity."
        )

    if pd.notna(sleep_disorder):
        recommendations.append(
            "Consider discussing the reported sleep "
            "disorder with a healthcare professional."
        )
#base case
    if not recommendations:
        recommendations.append(
            "Maintain your current sleep and lifestyle habits."
        )

    return " ".join(recommendations)