import random


def generate_password():
    random_pass = random.randint(100000, 999999)
    return random_pass


def generate_email():
    random_email = f"valeriakarapetyan{random.randint(100, 999)}@yandex.ru"
    return random_email
