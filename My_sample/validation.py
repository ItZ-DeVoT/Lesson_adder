import re


def name_validator(name):
    if type(name) == str and re.match(r"^[a-zA-Z\s]{3,30}$", name):
        return name
    else:
        raise ValueError("Invalid Name")


def code_validator(code):
    if type(code) == int:
        return code
    else:
        raise ValueError("Invalid Code")


def day_validator(day):
    if type(day) == str and day in ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
        return day
    else:
        raise ValueError("Invalid day")


def start_time_validator(start_time):
    if type(start_time) == str and re.match("[0-2][0-9]:[0-5][0-9]", start_time):
        return start_time
    else:
        raise ValueError("Invalid start time")


def duration_validator(duration):
    if type(duration) == int and 60 <= duration <= 120:
        return duration
    else:
        raise ValueError("Invalid duration")


def teacher_validator(teacher):
    if type(teacher) == str and re.match(r"^[a-zA-Z\s]{3,30}$", teacher):
        return teacher
    else:
        raise ValueError("Invalid teacher")
