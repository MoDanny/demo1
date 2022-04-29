min_to_sec = 60
unit_of_measure = "seconds"
print(3 * min_to_sec)


def minute_in_seconds(number_of_minutes, add_comment):
    print(f"Calculating {number_of_minutes} * {min_to_sec} -> {number_of_minutes * min_to_sec} {unit_of_measure} {add_comment}")


minute_in_seconds("a", "Hallo Welt")
minute_in_seconds(5, "Hallo Welt")
minute_in_seconds(7, "Hallo Welt")
