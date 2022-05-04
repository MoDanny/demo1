timetable = {"hours": 24, "minutes": 1440, "seconds": 86400 }

def days_to_units(num_of_days, conversion_unit):

    try:
        return f"{num_of_days} days are {num_of_days * timetable[conversion_unit]} {conversion_unit}"
    except KeyError:
        return "Doofus"

def validate_and_execute():
    try:
        user_input_number = int(days_and_unit_dict["days"])
        calculated_value = days_to_units(user_input_number, days_and_unit_dict["unit"])
        print(calculated_value)
    except ValueError:
        print("Invalid Input")


user_input = ""
while user_input != "exit":
    user_input = input("Give me days and unit. e.g. 45:hours\n")
    # set - liste mit diskreten elementen - list hat [] aber ein set hat {}
    # list hat also eine Reihenfolge, set nicht. set ist eine Menge.
    days_and_unit = user_input.split(":")
    print(days_and_unit)
    days_and_unit_dict = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(days_and_unit_dict)
    validate_and_execute()
