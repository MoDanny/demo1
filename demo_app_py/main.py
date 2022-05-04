from lists import validate_and_execute, user_input_message


user_input = ""
while user_input != "exit":
    user_input = input(user_input_message)
    # set - liste mit diskreten elementen - list hat [] aber ein set hat {}
    # list hat also eine Reihenfolge, set nicht. set ist eine Menge.
    days_and_unit = user_input.split(":")
    days_and_unit_dict = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    validate_and_execute(days_and_unit_dict)
