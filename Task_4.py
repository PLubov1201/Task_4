def longest_word(user_string):
    words = user_string.split()
    longest_word = max(words, key=len)
    print(f"Самое длинное слово в строке: {longest_word}")


user_string = input('Введите фразу')

longest_word(user_string)


