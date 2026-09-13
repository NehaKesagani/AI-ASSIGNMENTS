import pandas as pd


class AQIReflexAgent:
   
    def perceive(self, aqi):
        
        # Perceive the current AQI.
    
        return aqi

    def decide(self, aqi):
        # Apply condition-action rules.

        # Missing AQI
        if aqi is None or pd.isna(aqi):

            return {
                "category": "Unknown",
                "action": (
                    "Insufficient air-quality data."
                )
            }


        if aqi <= 50:

            return {
                "category": "Good",
                "action": (
                    "Normal outdoor activities are fine."
                )
            }

        elif aqi <= 100:

            return {
                "category": "Satisfactory",
                "action": (
                    "Outdoor activities can continue normally."
                )
            }

        elif aqi <= 200:

            return {
                "category": "Moderate",
                "action": (
                    "Sensitive individuals should reduce prolonged exposure. ")
                    
                }

        elif aqi <= 300:

            return {
                "category": "Poor",
                "action": (
                    "Reduce prolonged outdoor activities."
                )
            }

        elif aqi <= 400:

            return {
                "category": "Very Poor",
                "action": (
                    "Avoid prolonged outdoor exposure."
                )
            }

        else:

            return {
                "category": "Severe",
                "action": (
                    "Avoid outdoor exposure and take precautions."
                            )
            }