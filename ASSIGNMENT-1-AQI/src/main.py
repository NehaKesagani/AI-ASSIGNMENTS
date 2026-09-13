from preprocessing import (
    load_data,
    preprocess_data
)

from feature_engineering import create_features

from reflex_agent import AQIReflexAgent


DATA_PATH = "data/city_day.csv"
OUTPUT_PATH = "data/aqi_agent_output.csv"


def main():
    print("        AQI SIMPLE REFLEX AGENT")
    # Load dataset
    print("\nLoading dataset...")

    df = load_data(DATA_PATH)

    print(f"Original rows: {len(df)}")
    print(f"Number of cities: {df['City'].nunique()}")

    #  Preprocessing
    print("\nPreprocessing data...")

    df = preprocess_data(df)

    print(
        f"Rows after preprocessing: {len(df)}"
    )

    
    # Feature Engineering
    print("\nCalculating AQI features...")

    df = create_features(df)

    # Simple Reflex Agent
    
    print("Running Simple Reflex Agent...")

    agent = AQIReflexAgent()

    decisions = df["Calculated_AQI"].apply(
        agent.decide
    )

    df["AQI_Category"] = decisions.apply(
        lambda result: result["category"]
    )

    df["Agent_Action"] = decisions.apply(
        lambda result: result["action"]
    )

    # Create agent output
    
    agent_output = df[
        [
            "City",
            "Date",
            "Calculated_AQI",
            "Dominant_Pollutant",
            "AQI_Category",
            "Agent_Action"
        ]
    ].copy()

    # Save agent output
    
    agent_output.to_csv(
        OUTPUT_PATH,
        index=False
    )
    # Displaying one sample from each city
    
    print("       SAMPLE AGENT OUTPUT")
    sample_output = (
        agent_output
        .groupby("City", sort=True)
        .head(1)
    )

    print(
        sample_output.to_string(index=False)
    )

    print("Processing completed successfully!")
    print(
        f"\nAgent output saved to:"
        f"\n{OUTPUT_PATH}"
    )

    print(
        f"\nTotal records processed: "
        f"{len(agent_output)}"
    )


if __name__ == "__main__":
    main()