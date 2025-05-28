def count_words(text):
    #Подсчитывает количество слов в тексте.

    words = text.split()
    return len(words)

print("Number of words:", count_words("Это пример текста для подсчета слов."))