import time
import pandas as pd
import pymorphy3
import nltk
import csv
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

start = time.time()

# Загрузка необходимых ресурсов для работы nltk
nltk.download('punkt')
nltk.download('stopwords')

# Определение пунктуационных знаков и стоп-слов для русского языка
punctuation_marks = ['!', ',', '(', ')', ':', '-', '?', '.', '..', '...', '«', '»', '#']
stop_words = stopwords.words("russian")
morph = pymorphy3.MorphAnalyzer()

# Функция для предобработки текста: токенизация, лемматизация, удаление стоп-слов и пунктуации
def preprocess(text, stop_words, punctuation_marks, morph):
    tokens = word_tokenize(text.lower())
    preprocessed_text = ""
    for token in tokens:
        if token not in punctuation_marks:
            lemma = morph.parse(token)[0].normal_form
            if lemma not in stop_words:
                preprocessed_text = preprocessed_text + lemma + " "
    return preprocessed_text

# Загрузка словаря слов из файла и приведение их к нормальной форме
def lems():
    words = set()
    with open('words.csv', 'r', encoding='utf-8') as words_file:
        reader = csv.reader(words_file)
        for row in reader:
            for word in row:
                normalized_word = morph.parse(word)[0].normal_form
                words.add(normalized_word)
    print(words)

    # Чтение постов из CSV файла и применение функции предобработки к каждому посту
    posts = pd.read_csv('vk_posts.csv', sep=",", names=['text'])
    post1 = posts.dropna()
    bank = post1['text'].apply(lambda text: preprocess(text, stop_words, punctuation_marks, morph))
    print(bank)

    # Запись леммантизированных постов в новый CSV файл с ключевыми словами веденными пользователем
    unique_posts = set()  # Создание множества для хранения уникальных постов
    with open('vk_posts_normal.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['text'])
        count = 0
        for post_text in bank:
            post_words = set(post_text.split())
            if words.intersection(post_words) and post_text not in unique_posts:
                writer.writerow([post_text])
                unique_posts.add(post_text)  # Добавление поста в множество уникальных постов
                count += 1
                if count == 511:  # Завершение цикла после записи 511 уникальных постов
                    break



end = time.time()
print("lemm",end-start)