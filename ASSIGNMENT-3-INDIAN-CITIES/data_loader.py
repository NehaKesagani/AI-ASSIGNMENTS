import pandas as pd
df = pd.read_csv("indian_cities_dataset.csv")
print(df.head())
print("\nNumber of road connections:", len(df))
cities = set(df["Source"]) | set(df["Destination"])
print("Number of cities:", len(cities))
print("\nCities:")
print(sorted(cities))