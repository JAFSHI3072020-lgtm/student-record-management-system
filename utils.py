def get_non_empty_string(prompt):
    while True:
        value = input(prompt).strip()
        if value.isalpha() or " " in value:
            return value
        print("Error: Input must be a valid string.")


def get_valid_roll(prompt):
    while True:
        roll = input(prompt).strip()
        if roll.isdigit():
            return int(roll)
        print("Error: Roll number must be an integer.")


def get_email(prompt):
    while True:
        email = input(prompt).strip()
        if "@" in email and "." in email:
            return email
        print("Error: Invalid email format.")
