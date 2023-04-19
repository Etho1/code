#ETHAN SPENCER CSE111


# Define a dictionary to store the recommended daily calorie intake based on activity level
es_calorie_intake = {
    "sedentary": 1.2,
    "lightly active": 1.375,
    "moderately active": 1.55,
    "very active": 1.725,
    "extra active": 1.9
}

# Define a function to convert height from feet/inches to centimeters
def es_convert_height_to_cm(es_height, es_country):
    if es_country.lower() == "united states":
        es_height = es_height * 2.54 # convert inches to centimeters
    return es_height

# Define a function to convert weight from lbs to kgs
def es_convert_weight_to_kg(es_weight, es_country):
    if es_country.lower() == "united states":
        es_weight = es_weight * 0.453592 # convert lbs to kgs
    return es_weight

# Define a function to calculate basal metabolic rate (BMR) based on user's sex, weight, and height
def es_calculate_bmr(es_sex, es_weight, es_height, es_age):
    if es_sex.lower() == "male":
        es_bmr = (10 * es_weight) + (6.25 * es_height) - (5 * es_age) + 5
    elif es_sex.lower() == "female":
        es_bmr = (10 * es_weight) + (6.25 * es_height) - (5 * es_age) - 161
    else:
        print("Invalid sex input")
        return None
    return es_bmr

# Define a function to adjust BMR based on user's ethnicity
def es_adjust_bmr_by_ethnicity(es_bmr, es_ethnicity):
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
        return None
    return es_bmr

# Define a function to calculate the recommended daily calorie intake based on user's activity level
def es_calculate_calorie_intake(es_bmr, es_activity_level):
    if es_activity_level.lower() in es_calorie_intake:
        es_calorie_intake_factor = es_calorie_intake[es_activity_level.lower()]
    else:
        print("Invalid activity level input")
        return None
    es_recommended_calorie_intake = round(es_bmr * es_calorie_intake_factor)
    return es_recommended_calorie_intake

# Define a function to prompt user for input and call other functions to calculate recommended calorie intake
def main():
    es_height = float(input("What is your height (in feet and inches if you are in the United States) or in centimeters? "))
    es_weight = float(input("What is your weight (in pounds if you are in the United States) or in kilograms? "))
    es_sex = input("What is your sex (male or female)? ")
    es_age = int(input("What is your age? "))
    es_ethnicity = input("What is your ethnicity (white, black, Hispanic, or Asian)? ")
    es_country = input("What is your country of residence? ")
    es_activity_level = input("How would you describe your activity level (sedentary, lightly active, moderately active, very active, or extra active)? ")
    
    # Convert height to centimeters and weight to kilograms
    es_height = es_convert_height_to_cm(es_height, es_country)
    es_weight = es_convert_weight_to_kg(es_weight, es_country)
    
    # Calculate basal metabolic rate (BMR)
    es_bmr = es_calculate_bmr(es_sex, es_weight, es_height, es_age)
    if es_bmr is None:
        return None
    
    # Adjust BMR based on ethnicity
    es_bmr = es_adjust_bmr_by_ethnicity(es_bmr, es_ethnicity)
    if es_bmr is None:
        return None
    
    # Calculate recommended daily calorie intake
    es_recommended_calorie_intake = es_calculate_calorie_intake(es_bmr, es_activity_level)
    return es_recommended_calorie_intake

if __name__ == "__main__":
    main()
