demo_list = ["Omega", "abc", "xyz", "Omega"]
element = demo_list[0]
print(demo_list)
print(element)
print(demo_list[2])
demo_list.append("Theta")
demo_list.append("Epsilon")
print(demo_list)
demo_list.remove("Omega")
print(demo_list)
demo_list.remove("Omega")
print(demo_list)

print("********************************************** Sets")
demo_set = {"abc", "xyz", "Omega"}
print(demo_set)

for element in demo_set:
    print(element)

demo_set.add("Salbei")
print(demo_set)
try:
    demo_set.remove("Omega")
except KeyError:
    print("notinlist")
print(demo_set)

print("Hallo Welt".replace("Welt", "Elch"))

print("********************************************** Dictionary")
demo_dict = {"days": 10,
             "hours": 4,
             "Notb": 666}

print(demo_dict)
print(type(demo_dict))

# Modules #
timetable = {"hours": 24, "minutes": 1440, "seconds": 86400}
user_input_message = "Give me days and unit. e.g. 45:hours\n"


def days_to_units(num_of_days, conversion_unit):
    try:
        return f"{num_of_days} days are {num_of_days * timetable[conversion_unit]} {conversion_unit}"
    except KeyError:
        return "Doofus"


def validate_and_execute(days_and_unit_dict):
    try:
        user_input_number = int(days_and_unit_dict["days"])
        calculated_value = days_to_units(user_input_number, days_and_unit_dict["unit"])
        print(calculated_value)
    except ValueError:
        print("Invalid Input")
