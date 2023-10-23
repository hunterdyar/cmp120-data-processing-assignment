# Empty placeholder for student use.

def number_to_day_of_week(num):
    if num == 1:
        return "Monday"
    if num == 2:
        return "Tuesday"
    if num == 3:
        return "Wednesday"
    if num == 4:
        return "Thursday"
    if num == 5:
        return "Friday"
    if num == 6:
        return "Saturday"
    if num == 7:
        return "Sunday"

    raise ValueError(f"Error. Could not convert {num} into weekday. Is it an integer?")
