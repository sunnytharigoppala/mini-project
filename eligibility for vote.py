def calculate_bmi(weight, height):
    """
Calculate Body Mass Index (BMI)
Parameters:
 weight (float): Weight in kilograms
 height (float): Height in meters
Returns:
 float: BMI value
    """
bmi = weight / (height ** 2)
return round(bmi, 2)
bmi = calculate_bmi(70, 1.75)
print(f"BMI: {bmi}")