import os.path
from datetime import datetime, timedelta
import random
import re
from flask import Flask

app = Flask(__name__)
cats_List = ["корниш-рекс", "русская голубая", "шотландская вислоухая", "мейн-кун", "манчкин"]
cars_list = ["Chevrolet", "Renault", "Ford", "Lada"]
counter = 0
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


@app.route('/hello_world')
def show_hello_world():
    return "Привет, мир!"


@app.route('/cars')
def show_cars_list():
    return ", ".join(cars_list)


@app.route('/cats')
def get_random_cat():
    return random.choice(cats_List)


@app.route('/get_time/now')
def get_current_time():
    current_time = datetime.now().time()
    return f"Точное время: {current_time}"


@app.route('/get_time/future')
def get_future_time():
    current_time = datetime.now()
    added_time = timedelta(hours=1)
    current_time_after_hour = (current_time + added_time).time()
    return f"Точное время через час будет {current_time_after_hour}"


@app.route('/get_random_word')
def get_random_word():
    BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt')
    with open(BOOK_FILE, 'r', encoding='utf-8') as file:
        res = re.findall(r"\w+", file.read())
        print(BASE_DIR)
        return random.choice(res)


@app.route('/counter')
def update_counter():
    global counter
    counter += 1
    return f'Эту страницу открыли {counter} раз(а)'


if __name__ == '__main__':
    app.run(debug=True)
