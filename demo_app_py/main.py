min_to_sec = 2 * 5 * 6
unit_of_measure = "seconds"
print(3 * min_to_sec)


def minute_in_seconds(number_of_minutes):
    if number_of_minutes > 0:
        return f"Calculating {number_of_minutes} * {min_to_sec} -> {number_of_minutes * min_to_sec} {unit_of_measure}"
    elif number_of_minutes == 0:
        return "No Zero allowed"

def validate_and_execute():
    if user_input.isdigit():
        user_input_number = int(user_input)
        result = minute_in_seconds(user_input_number)
        print(result)
    else:
        print("meh!!!")

user_input = input("Give me input:\n")
validate_and_execute()

