import pandas as pd


# Pollutants used for AQI calculation
AQI_POLLUTANTS = [
    "PM2.5",
    "PM10",
    "NOx",
    "NH3",
    "CO",
    "SO2",
    "O3",
]


def load_data(file_path):
    # Load the AQI dataset from a CSV file.

    return pd.read_csv(file_path)


def preprocess_data(df):
    
    df = df.copy()

    # Convert Date
    df["Date"] = pd.to_datetime(
        df["Date"],
        errors="coerce"
    )

    # Convert pollutant columns to numeric
    for column in AQI_POLLUTANTS:

        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )

    # Remove rows where every AQI pollutant is missing
    df = df.dropna(
        subset=AQI_POLLUTANTS,
        how="all"
    )

    # Sort chronologically
    df = df.sort_values(
        ["City", "Date"]
    ).reset_index(drop=True)

    return df