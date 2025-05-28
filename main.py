import random
import string

version = "1.0"

def generate_password(length=12):
    #Генерирует случайный пароль из букв, цифр и специальных символов.

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("Generated Password:", generate_password())