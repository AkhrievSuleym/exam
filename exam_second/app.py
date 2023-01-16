"""Проверка"""
from flask import Flask, render_template, request

app = Flask(__name__)
def word_izo(word):
    """Проверка слова. Является ли оно изограммой?"""
    letters = [item.lower() for item in word]
    set_select = set(letters)
    if len(letters) == len(set_select):
        return True
    else:
        return False

@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == "POST":
        first_word = request.form['word']
        answer = word_izo(first_word)
        return render_template('index.html', answer = answer)
    else:
        return render_template('index.html')

app.run()