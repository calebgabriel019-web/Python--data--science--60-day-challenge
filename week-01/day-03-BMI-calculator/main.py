def get_bmi_category(bmi):
    if bmi <= 18.5:
        return ("Underweight")
    elif bmi <= 24.9:
        return ("Normal weight")
    elif bmi <=  29.0:
        return (" Overweight")
    else:
        return (" Obesity")



def bmi_calculator():
    print(" Welcome this is a BMI caculator")
    unit = input("Chooose a unit either (M)etric kg/m or (I)mperial ibs/in: ").strip()   .lower()


    try:
        if unit == "m":
            weight = float(input("Enter the weight in kg: "))
            height = float(input("Enter the height in meters: "))
            bmi = weight / (height) ** 2
        elif unit == "i":
            weight == float(input("Enter te weight in lbs:"))
            height = float(input("Enter the height in inches: "))
            bmi = weight / (height) ** 2
        else:
            print("error : it mut be either m or i")
        print(f" the bmi is{bmi}:.2f")
        print(f"the bmi category is {get_bmi_category(bmi)}   ")
    except ValueError as error:
        print(" Invalid input: please enter a numeric value")
bmi_calculator()   