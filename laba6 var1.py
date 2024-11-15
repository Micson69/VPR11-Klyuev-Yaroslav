# вар.11
# задание №1

def get_user_input():
    # Запрашиваем у пользователя строку
    user_input = input("Введите строку: ")
    return user_input

def validate_string(string):
    # Проверяем, что строка состоит только из русских букв
    valid_chars = [chr(i) for i in range(ord('а'), ord('я')+1)] + \
                  [chr(i) for i in range(ord('А'), ord('Я')+1)]
    for char in string:
        if char not in valid_chars and char != ' ':
            return False
    return True

def split_into_words(sentence):
    """Разделяем строку на слова"""
    words = []
    current_word = ""
    for char in sentence:
        if char.isalpha() or char == "'":
            current_word += char
        else:
            if current_word:
                words.append(current_word)
                current_word = ""
    if current_word:
        words.append(current_word)
    return words

def count_letters(word, letter):
    """Подсчет количества указанной буквы в слове"""
    count = 0
    for char in word:
        if char.lower() == letter:
            count += 1
    return count

def find_max_ab_words(words):
    """Находим слова с максимальной долей букв 'а' и 'б'"""
    max_ratio = 0
    result_words = []
    
    for word in words:
        count_a = count_letters(word, 'а')
        count_b = count_letters(word, 'б')
        total_length = len(word)
        
        if total_length == 0:
            continue
        
        ratio = (count_a + count_b) / total_length
        
        if ratio > max_ratio:
            max_ratio = ratio
            result_words.clear()
            result_words.append(word)
        elif ratio == max_ratio:
            result_words.append(word)
    
    return result_words

# Основной блок программы
if __name__ == "__main__":
    while True:
        user_input = get_user_input()
        
        if not validate_string(user_input):
            print("Некорректная строка! Введены недопустимые символы.")
            continue
        
        words = split_into_words(user_input)
        words_with_max_ab = find_max_ab_words(words)
        
        print(f"Исходная строка: {user_input}")
        print(f"Слова с максимальной долей 'а' и 'б': {' '.join(words_with_max_ab)}")