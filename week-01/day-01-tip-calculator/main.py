
def calculate_tip_and_split_calculator():

    print("Welcome to the tip calculator!")
    bill = float(input("What was the total bill? $"))
    tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
    people = int(input("How many people to split the bill? "))

    tip_amount = bill * (tip_percentage / 100)
    total_bill = bill + tip_amount
    amount_per_person = total_bill / people

    print(f"Each person should pay: ${amount_per_person:.2f}")

calculate_tip_and_split_calculator()

