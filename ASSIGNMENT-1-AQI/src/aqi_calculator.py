#AQI Calculator

# Converts pollutant concentrations into AQI sub-indices using breakpoint-based linear interpolation.

# The overall AQI is the highest pollutant sub-index.
# AQI BREAKPOINT Format: (concentration_low, concentration_high,AQI_low, AQI_high)

BREAKPOINTS = {

    "PM2.5": [
        (0, 30, 0, 50),
        (31, 60, 51, 100),
        (61, 90, 101, 200),
        (91, 120, 201, 300),
        (121, 250, 301, 400),
        (251, 380, 401, 500),
    ],

    "PM10": [
        (0, 50, 0, 50),
        (51, 100, 51, 100),
        (101, 250, 101, 200),
        (251, 350, 201, 300),
        (351, 430, 301, 400),
        (431, 510, 401, 500),
    ],

    "NOx": [
        (0, 40, 0, 50),
        (41, 80, 51, 100),
        (81, 180, 101, 200),
        (181, 280, 201, 300),
        (281, 400, 301, 400),
        (401, 500, 401, 500),
    ],

    "NH3": [
        (0, 200, 0, 50),
        (201, 400, 51, 100),
        (401, 800, 101, 200),
        (801, 1200, 201, 300),
        (1201, 1800, 301, 400),
        (1801, 2400, 401, 500),
    ],

    "CO": [
        (0, 1.0, 0, 50),
        (1.1, 2.0, 51, 100),
        (2.1, 10, 101, 200),
        (10.1, 17, 201, 300),
        (17.1, 34, 301, 400),
        (34.1, 50, 401, 500),
    ],

    "SO2": [
        (0, 40, 0, 50),
        (41, 80, 51, 100),
        (81, 380, 101, 200),
        (381, 800, 201, 300),
        (801, 1600, 301, 400),
        (1601, 2100, 401, 500),
    ],

    "O3": [
        (0, 50, 0, 50),
        (51, 100, 51, 100),
        (101, 168, 101, 200),
        (169, 208, 201, 300),
        (209, 748, 301, 400),
        (749, 1000, 401, 500),
    ],
}


def calculate_sub_index(concentration, breakpoints):
    
    """Calculate AQI sub-index using linear interpolation Formula: 

    Ip = ((IHI - ILO) / (BHI - BLO))
         * (Cp - BLO) + ILO
    """

    if concentration is None:
        return None

    if concentration != concentration:
        return None

    if concentration < 0:
        return None

    for (
        bp_low,
        bp_high,
        aqi_low,
        aqi_high
    ) in breakpoints:

        if bp_low <= concentration <= bp_high:

            aqi = (
                ((aqi_high - aqi_low)
                 / (bp_high - bp_low))
                * (concentration - bp_low)
                + aqi_low
            )

            return round(aqi, 2)

    # Values above the highest breakpoint
    if concentration > breakpoints[-1][1]:
        return 500.0

    return None


def calculate_overall_aqi(row):
    """
    Calculate AQI from all available pollutant values.Overall AQI = maximum pollutant sub-index.
    """

    sub_indices = {}

    for pollutant, breakpoints in BREAKPOINTS.items():

        value = row.get(pollutant)

        sub_index = calculate_sub_index(
            value,
            breakpoints
        )

        if sub_index is not None:
            sub_indices[pollutant] = sub_index

    if not sub_indices:
        return None

    return max(sub_indices.values())


def find_dominant_pollutant(row):
    # Find the pollutant contributing the highest AQIsub-index.
   

    sub_indices = {}

    for pollutant, breakpoints in BREAKPOINTS.items():

        value = row.get(pollutant)

        sub_index = calculate_sub_index(
            value,
            breakpoints
        )

        if sub_index is not None:
            sub_indices[pollutant] = sub_index

    if not sub_indices:
        return "Unknown"

    return max(
        sub_indices,
        key=sub_indices.get
    )