import pandas as pd
import numpy as np

# Dummy function simulating a more complex recommendation engine
def personalized_recommendations(preferences):
    # Dummy data
    properties_db = pd.DataFrame([
        {"location": "San Francisco", "price": 950000, "type": "condo", "bedrooms": 2},
        {"location": "San Francisco", "price": 800000, "type": "apartment", "bedrooms": 2},
        {"location": "San Francisco", "price": 1200000, "type": "condo", "bedrooms": 3},
    ])
    
    # Filter properties based on user preferences
    results = properties_db[
        (properties_db['location'] == preferences['location']) &
        (properties_db['price'] <= preferences['budget']) &
        (properties_db['type'] == preferences['property_type']) &
        (properties_db['bedrooms'] == preferences['bedrooms'])
    ]
    
    return results.to_dict(orient='records')
