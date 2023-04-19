# Define a dictionary to store the recommended daily calorie intake based on activity level
es_calorie_intake = {
    "sedentary": 1.2,
    "lightly active": 1.375,
    "moderately active": 1.55,
    "very active": 1.725,
    "extra active": 1.9
}

# Define a function to calculate the recommended daily calorie intake based on the user's input
def calculate_calorie_intake(es_height, es_weight, es_sex, es_ethnicity, es_country, es_activity_level):
    # Convert height and weight to metric if the user is in the United States
    if es_country.lower() == "united states":
        es_height = height * 2.54 # convert inches to centimeters
        es_weight = weight * 0.453592 # convert lbs to kgs
    
    # Calculate the user's basal metabolic rate (BMR) using the Mifflin-St Jeor equation
    if es_sex.lower() == "male":
        es_bmr = (10 * es_weight) + (6.25 * es_height) - (5 * 25) + 5
    elif es_sex.lower() == "female":
        es_bmr = (10 * es_weight) + (6.25 * es_height) - (5 * 25) - 161
        
        # Adjust BMR based on ethnicity
        if es_ethnicity.lower() == "white":
            es_bmr -= 5
        elif es_ethnicity.lower() == "black":
            es_bmr -= 161
        elif es_ethnicity.lower() == "hispanic":
            es_bmr -= 21
        elif es_ethnicity.lower() == "asian":
            es_bmr += 88
        else:
            print("Invalid ethnicity input")
            return
    
    # Multiply the BMR by the activity level factor from the dictionary
    if es_activity_level.lower() in es_calorie_intake:
        es_calorie_intake_factor = es_calorie_intake[activity_level.lower()]
    else:
        print("Invalid activity level input")
        return
        
    recommended_calorie_intake = round(es_bmr * es_calorie_intake_factor)
    
    # Print the recommended daily calorie intake for the user
    print(f"Based on your input, your recommended daily calorie intake is {recommended_calorie_intake} calories.")
    
# Prompt the user for their height, weight, sex, ethnicity, country of residence, and activity level
height = float(input("What is your height (in feet and inches if you are in the United States) or in centimeters? "))
weight = float(input("What is your weight (in pounds if you are in the United States) or in kilograms? "))
sex = input("What is your sex (male or female)? ")
ethnicity = input("What is your ethnicity (white, black, Hispanic, or Asian)? ")
country = input("What is your country of residence? ")
activity_level = input("What is your activity level (sedentary, lightly active, moderately active, very active, or extra active)? ")

# Call the calculate_calorie_intake function with the user's input as arguments
calculate_calorie_intake(height, weight, sex, ethnicity, country, activity_level)
