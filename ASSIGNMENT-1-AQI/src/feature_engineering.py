from aqi_calculator import (
    BREAKPOINTS,
    calculate_sub_index,
    calculate_overall_aqi,
    find_dominant_pollutant,
)


def create_features(df):
    """
    Generated features:
        PM2.5_AQI
        PM10_AQI
        NOx_AQI
        NH3_AQI
        CO_AQI
        SO2_AQI
        O3_AQI

        Calculated_AQI
        Dominant_Pollutant
    """

    df = df.copy()
    # Pollutant-specific AQI sub-indices
    
    for pollutant, breakpoints in BREAKPOINTS.items():

        feature_name = f"{pollutant}_AQI"

        df[feature_name] = df[pollutant].apply(
            lambda value: calculate_sub_index(
                value,
                breakpoints
            )
        )
    # Overall AQI
    
    df["Calculated_AQI"] = df.apply(
        calculate_overall_aqi,
        axis=1
    )

    # Dominant pollutant
    
    df["Dominant_Pollutant"] = df.apply(
        find_dominant_pollutant,
        axis=1
    )

    return df