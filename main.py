import re

def is_palindrome(text):
    #Проверяет, является ли строка палиндромом, игнорируя пробелы и регистр.

    cleaned = re.sub(r'[^a-zA-Z0-9]', '', text).lower()
    return cleaned == cleaned[::-1]

print("Is 'А роза упала на лапу Азора' a palindrome?", is_palindrome("А роза упала на лапу Азора"))