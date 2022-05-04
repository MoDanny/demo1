calculation_to_units = 24
name_of_unit = "hours"
demo_list = ["abc", "xyz", "Omega"]
element1 = demo_list[0]
print (element1)
print(demo_list[2])
demo_list.append("Theta")
print(demo_list)


def days_to_units(num_of_days):
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"
    elif num_of_days == 0:
        return "Zero (0) is not allowed"
    else:
        return "Negative Number"

def validate_and_execute():
    try:
        user_input_number = int(number_of_days_element)
        calculated_value = days_to_units(user_input_number)
        print(calculated_value)
    except ValueError:
        print("Invalid Input")


user_input = ""
while user_input != "exit":
    user_input = input("Give me input comma separated:\n")
    for number_of_days_element in user_input.split(", "):
        validate_and_execute()