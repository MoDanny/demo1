min_to_sec = 60
unit_of_measure = "seconds"
print(3 * min_to_sec)


def minute_in_seconds(user_input):
    print(f"Calculating {user_input} * {min_to_sec} -> {user_input * min_to_sec} {unit_of_measure}")


minute_in_seconds(3)
minute_in_seconds(5)
minute_in_seconds(7)
