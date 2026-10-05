import pandas as pd
from pathlib import Path
#load datasset
print("starting dataset overview")
def load_dataset():
    base_dir = Path(__file__).resolve().parent.parent
    data_path = r"C:\Users\Neha Kesagani\Desktop\SEM 1\EOAI\Assignemts\ASSIGNMENT-2 SLEEP SCORE\Sleep_health_and_lifestyle_dataset.csv"

    df = pd.read_csv(data_path)

    return df


def display_dataset_overview(df):
    print("=" * 60)
    print("DATASET OVERVIEW")
    print("=" * 60)

    print("\nDataset Shape:")
    print(df.shape)

    print("\nColumns:")
    for column in df.columns:
        print("-", column)

    print("\nAge Range:")
    print(f"Minimum Age: {df['Age'].min()}")
    print(f"Maximum Age: {df['Age'].max()}")

    print("\nSleep Duration:")
    print(f"Minimum: {df['Sleep Duration'].min()} hours")
    print(f"Maximum: {df['Sleep Duration'].max()} hours")
    print(f"Average: {df['Sleep Duration'].mean():.2f} hours")

    print("\nStress Level:")
    print(f"Minimum: {df['Stress Level'].min()}")
    print(f"Maximum: {df['Stress Level'].max()}")
    print(f"Average: {df['Stress Level'].mean():.2f}")

    print("\nPhysical Activity:")
    print(
        f"Minimum: {df['Physical Activity Level'].min()}"
    )
    print(
        f"Maximum: {df['Physical Activity Level'].max()}"
    )
    print(
        f"Average: {df['Physical Activity Level'].mean():.2f}"
    )

#missing values check 
def display_missing_values(df):
    print("\n" + "=" * 60)
    print("MISSING VALUES")
    print("=" * 60)

    print(df.isnull().sum())