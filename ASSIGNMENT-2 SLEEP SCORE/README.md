## Introduction
Sleep Score Intelligent Agent is a **model based intelligent agent** that evaluates an individual's sleep and lifestyle conditions.
It calculates  sleep score, classifies the person's sleep condition, explains the factors and provides suitable recommendations.

The project uses the **Sleep Health and Lifestyle Dataset** to understand the relevant sleep and lifestyle features and design the agent's internal model.

## Problem Statement

Develop an intelligent agent that accepts sleep and lifestyle information of different individuals, calculate a Sleep Score, categorizes their sleep condition, and provides personalized recommendations.

## Modules

| Module                   | Function        
| `dataset_overview.py`    | Loads the dataset and provides basic dataset information. 
| `feature_engg.py`        | Converts raw inputs into normalized component scores. 
| `sleep_score.py`         | Combines component scores and determines the Sleep Category. 
| `agent_explanation.py`   | Identifies contributing factors and generates recommendations. 
| `Iagent.py`               | Integrates scoring,classification, reasoning andrecommendation. 
| `main.py`                | Takes user input and displays the final agent result. 

### Work Flow

Input
  ↓
Feature Engineering
  ↓
Internal Sleep Model
  ↓
Sleep Score
  ↓
Sleep Category
  ↓
Reasoning
  ↓
Recommendation


## Assumptions
- 8 hours is used as the reference sleep duration.
- Sleep Duration has a weight of 40%.
- Stress Level has a weight of 25%.
- Physical Activity has a weight of 20%.
- Sleep Disorder has a weight of 15%.
- Physical activity of 60 minutes/day or more is considered good.
- Stress level 1–4 is considered low, 5–6 moderate, and 7–10 high.

## Sample input and output

Enter the person's details:

Age: 31
Sleep Duration (hours): 6
Stress Level (1-10): 5
Physical Activity Level (minutes/day): 20
Sleep Disorder (None / Insomnia / Sleep Apnea): None
Sleep Analysis Result:

Age: 31
Sleep Score: 53.33/100
Sleep Category: Moderate

Reason:
low sleep duration, moderate stress, no proper physical activity, no sleep disorder recorded

Recommendation:
Try to increase your sleep duration. Consider increasing your physical activity.
