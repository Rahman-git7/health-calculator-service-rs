
def calculate_bmi(height, weight):
    """Calculate BMI (Body Mass Index) from height in meters and weight in kilograms."""
    return weight / (height ** 2)

def calculate_bmr(height, weight, age, gender):
    """Calculate BMR (Basal Metabolic Rate) using the Harris-Benedict equation."""
    if gender.lower() == 'male':
        return 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    elif gender.lower() == 'female':
        return 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    else:
        raise ValueError("Gender must be 'male' or 'female'")
