from flask import Flask, render_template, request, jsonify
import csv

from pars_vk import get_posts
from lemma_form import lems
from hug import chat

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template("index.html")

@app.route('/button_click', methods=['POST'])
def process_url():
    data = request.json
    word_input = data.get('wordInput')
    prompt_input = data.get('promptInput')
    selected_groups = data.get('groups')
    print(selected_groups)
    if selected_groups:
        for group in selected_groups:
            parser = get_posts(group)
    lems()
    chat(prompt_input)  # Используем prompt_input здесь
    with open('words_gpt.csv', 'r', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        words = [row for row in csvreader]
    print(words)
    return jsonify({'words': words})

@app.route('/add_word', methods=['POST'])
def add_word():
    word = request.form.get('word')
    entered_words = []
    if word:
        entered_words.append(word)
        for i in entered_words:
            entered_words = i.split()
        with open('words.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(entered_words)
        print('Массив введенных слов:', entered_words)
        return 'Слово успешно добавлено в массив'
    else:
        return 'Введите слово!'

if __name__ == "__main__":
    app.run(debug=True)
