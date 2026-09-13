# AQI Simple Reflex Agent

##  Project Overview

## AIM:
This project implements a Simple Reflex Agent for Air Quality Index (AQI) using real-world air-quality data from Indian cities.

## Goal:
The main objective of the project is to demonstrate how an intelligent agent can perceive the current state of its environment and take an appropriate action using predefined condition-action rules.

The agent does not use historical reasoning, prediction, learning, or internal memory. Instead, it follows the principle of a Simple Reflex Agent:
 Current percept → Condition → Action

# Problem Statement

Air pollution contains multiple pollutants such as:

* PM2.5
* PM10
* NOx
* NH3
* CO
* SO2
* O3

Different pollutants have different concentration ranges and health impacts.

The objective of this project is to:

1. Load and preprocess air-quality data.
2. Calculate pollutant-specific AQI sub-indices.
3. Calculate an overall AQI from the available pollutant measurements.
4. Identify the dominant pollutant.
5. Use the calculated AQI as the percept for a Simple Reflex Agent.
6. Classify the air quality into an AQI category.
7. Generate an appropriate action using condition-action rules.
8. Save the resulting agent decisions into a clean output CSV file.

#  Dataset Used

Air Quality Data in India – City Day Dataset

The dataset is commonly available as `city_day.csv` and contains daily air-quality measurements from multiple Indian cities.

The dataset contains:

* 29,531 rows
* 16 columns
* 26 cities

# Why This Dataset Was Selected?

This dataset was selected because it is suitable for demonstrating an intelligent agent in an environmental monitoring scenario.
It provides:
* Multiple pollutant measurements.
* Data from many Indian cities.
* Daily observations.
* Real-world missing values.
* Sufficient features for preprocessing and feature engineering.

# Important Dataset Decision

The AQI calculation implemented in this project uses the following seven pollutants:

* PM2.5
* PM10
* NOx
* NH3
* CO
* SO2
* O3

The original `AQI` and `AQI_Bucket` columns are also not used as inputs to the reflex agent.

This avoids using the dataset's existing AQI value as the direct input for the agent's decision process.

# Workflow

The complete project follows this pipeline:


                    city_day.csv
                         │
                         ▼
                  Data Loading
                         │
                         ▼
                  Preprocessing
                         │
                         ▼
                Feature Engineering
                         │
                         ▼
               AQI Sub-index Calculation
                         │
                         ▼
                  Overall AQI
                         │
                         ▼
                Dominant Pollutant
                         │
                         ▼
               Simple Reflex Agent
                         │
                         ▼
                AQI Category + Action
                         │
                         ▼
                 Output CSV File

#  Software Engineering Approach

The project is organized into separate modules instead of putting all the logic inside one Python file.

This follows basic software engineering principles such as:

* Separation of concerns(Different tasks are placed in different modules)
* Modularity
* Code readability
* Reusability
* Meaningful naming of the files
* Configuration separation
* Clean input and output handling

# Project Structure
ASSIGNMENT-1 AQI/
│
├── data/
│   ├── city_day.csv
│   └── aqi_agent_output.csv
│
├── src/
│   ├── config.py
│   ├── preprocessing.py
│   ├── aqi_calculator.py
│   ├── feature_engineering.py
│   ├── reflex_agent.py
│   └── main.py
│
├── requirements.txt
├── .gitignore
└── README.md

# Description of Each File

## src/config.py

This file stores the AQI categories used by the project.

The categories are:

| AQI Range | Category     |
| --------: | ------------ |
|      0–50 | Good         |
|    51–100 | Satisfactory |
|   101–200 | Moderate     |
|   201–300 | Poor         |
|   301–400 | Very Poor    |
|   401–500 | Severe       |

Keeping these values separately makes the project easier to maintain and avoids scattering configuration values throughout the code.

# Data Preprocessing

The preprocessing logic is implemented in: src/preprocessing.py file
The preprocessing pipeline performs the following operations.

        Step 1 — Load the Dataset
        Step 2 — Convert Date
        Step 3 — Convert Pollutant Values to Numeric(Invalid values are converted to missing values rather than causing the complete program to fail)
        Step 4 — Handle Rows With No AQI Pollutant Information(Rows where **all seven AQI pollutants are missing** are removed.)
        Step 5 — Sort the Dataset(In chronological order)
# Dataset Processing Result
The original dataset contains:
        Rows: 29,531
        Cities: 26

After preprocessing, the project processes:
        Rows: 27,960

The difference is due to removing rows where all AQI-related pollutant measurements are missing.

#  Feature Engineering

Feature engineering is implemented in: src/feature_engineering.py file

Instead of directly using raw pollutant concentrations for the agent the project transforms pollutant concentrations into AQI sub-index features.

The following engineered features are generated: PM2.5_AQI, PM10_AQI, NOx_AQI, NH3_AQI, CO_AQI, SO2_AQI, O3_AQI
These features represent the AQI contribution of each pollutant.

Two additional features are generated:

        Calculated_AQI
        Dominant_Pollutant

Hence, here the feature engineering stage converts raw pollutant measurements into meaningful AQI-related information.

#  AQI Sub-index Calculation

The AQI calculator is implemented in: src/aqi_calculator.py file

Different pollutants have different concentration scales.
For example, the concentration of CO and the concentration of PM2.5 cannot simply be compared using their raw numerical values.
Hence, I used pollutant concentrations are mapped to AQI values using **AQI breakpoints**.

# AQI Breakpoints
A breakpoint defines a relationship between a pollutant concentration range and its corresponding AQI range.
# Linear Interpolation

When a pollutant concentration falls inside a breakpoint range, the corresponding AQI sub-index is calculated using linear interpolation.
The formula used is:

Ip = ((IHI - ILO) / (BHI - BLO))
     × (Cp - BLO) + ILO

Where:
        * `Ip` = pollutant AQI sub-index
        * `Cp` = pollutant concentration
        * `BLO` = lower concentration breakpoint
        * `BHI` = upper concentration breakpoint
        * `ILO` = lower AQI breakpoint
        * `IHI` = upper AQI breakpoint
This converts the pollutant concentration into a standardized AQI scale.

# Overall AQI

After calculating the AQI sub-index for each available pollutant, the project determines the overall AQI using:

Overall AQI = Maximum valid pollutant AQI sub-index

This means the pollutant contributing the highest AQI sub-index determines the overall air-quality level.
# Dominant Pollutant

This section identifies which pollutant produced the highest AQI sub-index and is stored in Dominant_pollutant.
# Simple Reflex Agent

The main intelligent-agent component is implemented in: src/reflex_agent.py file

 Condition-Action Rules used are:

|     AQI | Category     | Agent Action                                            |
| ------: | ------------ | ------------------------------------------------------- |
|    0–50 | Good         | Normal outdoor activities are fine.                     |
|  51–100 | Satisfactory | Outdoor activities can continue normally.               |
| 101–200 | Moderate     | Sensitive individuals should reduce prolonged exposure. |
| 201–300 | Poor         | Reduce prolonged outdoor activities.                    |
| 301–400 | Very Poor    | Avoid prolonged outdoor exposure.                       |
| 401–500 | Severe       | Avoid outdoor exposure and take precautions.            |


# Edge test case (Handling Missing AQI)

If an AQI value cannot be calculated because no usable pollutant information is available then the agent does not make an unsafe assumption.

Instead, it returns:
        Category: Unknown
        Action: Insufficient air-quality data.

This is a simple robustness measure for missing input.

# Output

The final agent output is saved as: data/aqi_agent_output.csv file

The output contains only the information relevant to the agent's decision:

| Column               | Description                          |
| -------------------- | ------------------------------------ |
| `City`               | City name                            |
| `Date`               | Observation date                     |
| `Calculated_AQI`     | AQI calculated by the project        |
| `Dominant_Pollutant` | Pollutant with highest AQI sub-index |
| `AQI_Category`       | Air-quality category                 |
| `Agent_Action`       | Action selected by the reflex agent  |

The raw input columns are not copied into the final agent output file because the output is intended to represent the agent's decision results rather than duplicate the entire source dataset.

# Main Program Flow

The complete execution is controlled by: src/main.py file
The program performs the following sequence:

        1. Load city_day.csv
                ↓
        2. Preprocess the data
                ↓
        3. Generate AQI sub-index features
                ↓
        4. Calculate overall AQI
                ↓
        5. Identify dominant pollutant
                ↓
        6. Send AQI to the reflex agent
                ↓
        7. Determine AQI category
                ↓
        8. Generate agent action
                ↓
        9. Save aqi_agent_output.csv

I had displayed a sample containing one processed record from each city for our understanding.
