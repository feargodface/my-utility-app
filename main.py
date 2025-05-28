version = "1.1"

def celsius_to_fahrenheit(celsius):
    #Конвертирует температуру из Цельсия в Фаренгейт.

    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    #Конвертирует температуру из Фаренгейта в Цельсий.

    return (fahrenheit - 32) * 5/9

print("100°C в Fahrenheit:", celsius_to_fahrenheit(100))
print("212°F в Celsius:", fahrenheit_to_celsius(212))