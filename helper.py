import random
import string


def generate_random_string(length):
    letters = string.ascii_uppercase
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string


def generate_mobile_number():
    return random.randint(1000000000, 9999999999)


def random_year_of_birth():
    return random.randint(1900, 2024)

