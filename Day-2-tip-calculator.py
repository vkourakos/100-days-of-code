print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?"))
tip_precent = float("1." + input("How much tip would you like to give? 10, 12, or 15?"))
num_of_people = int(input("How many people to split the bill?"))
tip_per_person = bill / num_of_people * tip_precent
tip_per_person = round(tip_per_person, 2)
print(f"Each person should pay: {tip_per_person}")
