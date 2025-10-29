import csv
import timeit
from hugchat import hugchat
from hugchat.login import Login


def chat(prompt_input):
    # Log in to huggingface and grant authorization to huggingchat
    EMAIL = ""
    PASSWD = ""
    cookie_path_dir = "./cookies/" # NOTE: trailing slash (/) is required to avoid errors
    sign = Login(EMAIL, PASSWD)
    cookies = sign.login(cookie_dir_path=cookie_path_dir, save_cookies=True)

    # Create your ChatBot
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())  # or cookie_path="usercookies/<email>.json"

    start = timeit.default_timer()

    key_words = set()

    prompt = ""  # Создаем пустую переменную для хранения объединенных строк

    with open('vk_posts_normal.csv', 'r', newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            for word in row:
                prompt += word + " "  # Добавляем содержимое каждой строки в переменную prompt

    preprompt = "Выдели из этого текста только фамилии, термины, организации, не пиши ничего кроме этих млов"
    if prompt_input:
        preprompt = prompt_input
    query_result = chatbot.chat(f"{preprompt}: {prompt}")
    for item in query_result["text"].split(", "):
        key_words.add(item)


    with open('words_gpt.csv', 'w', newline='', encoding='utf-8') as words_file:
        writer = csv.writer(words_file)
        for word in key_words:
            writer.writerow([word])

    stop = timeit.default_timer()
    print(key_words)
    print("Hugchat time:", stop - start)
