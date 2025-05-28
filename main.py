version = "1.1"

import random
import string
import re

def generate_password(length=12):
    #Генерирует случайный пароль из букв, цифр и специальных символов.

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def celsius_to_fahrenheit(celsius):
    #Конвертирует температуру из Цельсия в Фаренгейт.

    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    #Конвертирует температуру из Фаренгейта в Цельсий.

    return (fahrenheit - 32) * 5/9

def is_palindrome(text):
    #Проверяет, является ли строка палиндромом, игнорируя пробелы и регистр.

    cleaned = re.sub(r'[^a-zA-Z0-9]', '', text).lower()
    return cleaned == cleaned[::-1]

def count_words(text):
    #Подсчитывает количество слов в тексте.

    words = text.split()
    return len(words)

print("Generated Password:", generate_password())
print("100°C в Fahrenheit:", celsius_to_fahrenheit(100))
print("212°F в Celsius:", fahrenheit_to_celsius(212))
print("Is 'А роза упала на лапу Азора' a palindrome?", is_palindrome("А роза упала на лапу Азора"))
print("Number of words:", count_words("Это пример текста для подсчета слов."))