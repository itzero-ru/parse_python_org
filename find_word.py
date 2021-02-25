import re

def get_big_word(content):
    """Функция извлекает из строки самое длинное и часто слово
    
    - если есть несколько одинаковых позиций, то они так же выводятся
    """
    content = re.sub(r"\d+", "", content, flags=re.UNICODE).lower() # Убераем цифры и переводим все в нижний регистр

    if content.strip() == '': exit("Вы не передали текст")

    unique_words = set(re.findall(r'\w+', content))
    number_of_repetitions = 0 # Кол-во вхождений самого популярного слова
    dict_word = {}; list_word_len = {}

    for word in unique_words:
        dict_word[word] = number_of_matches = len(re.findall(r'\b{}\b'.format(word), content))
        list_word_len[word] = len(word)
        if number_of_matches > number_of_repetitions: number_of_repetitions = number_of_matches

    items_result = [item for item in dict_word if dict_word[item] == number_of_repetitions]
    
    print('\nЧаще всего встречается слово(-а) "{}"\nПовторяется(-ются) в тексте {} раз(-а)'.format(', '.join(items_result), number_of_repetitions))

    len_big_word = max(list_word_len.values()) # длина самого длиного слова в списке
    list_big_word = [big_word for big_word in list_word_len if list_word_len[big_word] == len_big_word] # Список самых длиных слов
    
    print('\nСамое длиное слово(-а): "{}"\n'.format(', '.join(list_big_word) ))


if(__name__ == __name__):
    
    print('Введите текст')
    get_big_word(input())