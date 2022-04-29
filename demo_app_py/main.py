min_to_sec = 2 * 5 * 6
unit_of_measure = "seconds"
print(3 * min_to_sec)


def minute_in_seconds(number_of_minutes):
    print(number_of_minutes > 0)
    if number_of_minutes > 0:
        return f"Calculating {number_of_minutes} * {min_to_sec} -> {number_of_minutes * min_to_sec} {unit_of_measure}"
    else:
        return("No Dice!")

#user_input = "b"
#minute_in_seconds("a")
#minute_in_seconds(user_input)

user_input = input("Give me input:\n")
user_input_number = int(user_input)
result = minute_in_seconds(user_input_number)
print(result)

