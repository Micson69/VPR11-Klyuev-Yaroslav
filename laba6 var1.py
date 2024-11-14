# вар.11
# задание №1

# Заданный список слов
words = []
while (word1 := input('Введите слово, которое добавиться в список(enter, чтобы остановит): ')) != '':
    words.append(word1)
print(words)

# Переменные для хранения максимальной доли и списка слов с этой долей
max_ratio = 0
max_ab_words = []

# Проходим по каждому слову
for word in words:
    for i in words:
        for j in i:
            if j 
    # Считаем количество букв 'а' и 'б'
    count_ab = 0
    for letter in word:
        if letter == 'а' or letter == 'б':
            count_ab += 1
    
    # Вычисляем длину слова
    length = 0
    for _ in word:
        length += 1
    
    # Вычисляем долю букв 'а' и 'б'
    if length > 0:
        ratio = count_ab / length
    else:
        ratio = 0

    # Если текущая доля больше максимальной, обновляем максимальную и очищаем список
    if ratio > max_ratio:
        max_ratio = ratio
        max_ab_words = [word]
    # Если текущая доля равна максимальной, добавляем слово в список
    elif ratio == max_ratio:
        max_ab_words.append(word)

# Результат
print("Слова с максимальной долей букв 'а' и 'б':", max_ab_words)

