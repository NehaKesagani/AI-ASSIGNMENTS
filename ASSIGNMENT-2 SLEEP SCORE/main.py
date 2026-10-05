from Iagent import analyze_person
#input
print("\nEnter the person's details:\n")

age = int(input("Age: "))

sleep_duration = float(
    input("Sleep Duration (hours): ")
)

stress_level = int(
    input("Stress Level (1-10): ")
)

activity_level = int(
    input("Physical Activity Level (minutes/day): ")
)

sleep_disorder = input(
    "Sleep Disorder (None / Insomnia / Sleep Apnea): "
).strip()


# Convert "None" to missing value
if sleep_disorder.lower() == "none":
    sleep_disorder = None
#analyse the person condition 
result = analyze_person(
    age=age,
    sleep_duration=sleep_duration,
    stress_level=stress_level,
    activity_level=activity_level,
    sleep_disorder=sleep_disorder
)
#agent result
print("Sleep Analysis Result:")
print(f"\nAge: {result['Age']}")
print(f"Sleep Score: {result['Sleep Score']}/100")
print(f"Sleep Category: {result['Sleep Category']}")

print("\nReason:")
print(result["Reason"])

print("\nRecommendation:")
print(result["Recommendation"])
