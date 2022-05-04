calculation_to_units = 24
name_of_unit = "hours"


def days_to_units(num_of_days):
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"
    elif num_of_days == 0:
        return "Zero (0) is not allowed"
    else:
        return "Negative Number"

def validate_and_execute():
    try:
        user_input_number = int(user_input)
        calculated_value = days_to_units(user_input_number)
        print(calculated_value)
    except ValueError:
        print("Invalid Input")


user_input = ""
while user_input != "exit":
    user_input = input("Give me input:\n")
    validate_and_execute()