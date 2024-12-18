from utils.property_discovery import personalized_recommendations
from utils.virtual_assistant import real_estate_query_assistant

def main():
    # Simulate user input for personalized property discovery
    user_preferences = {
        "location": "San Francisco",
        "budget": 1000000,
        "property_type": "condo",
        "bedrooms": 2
    }
    
    # Get property recommendations based on user preferences
    recommendations = personalized_recommendations(user_preferences)
    print("Recommended Properties:")
    for rec in recommendations:
        print(rec)

    # Simulate a user query to the virtual assistant
    user_query = "What is the average housing price in San Francisco?"
    response = real_estate_query_assistant(user_query)
    print(f"Assistant Response: {response}")

if __name__ == "__main__":
    main()
