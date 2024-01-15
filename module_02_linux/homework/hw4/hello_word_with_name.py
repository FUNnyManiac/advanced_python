"""
Реализуйте endpoint /hello-world/<имя>, который возвращает строку «Привет, <имя>. Хорошей пятницы!».
Вместо хорошей пятницы endpoint должен уметь желать хорошего дня недели в целом, на русском языке.

Пример запроса, сделанного в субботу:

/hello-world/Саша  →  Привет, Саша. Хорошей субботы!
"""

from flask import Flask
from datetime import datetime as date

app = Flask(__name__)


@app.route('/hello-world/<name>')
def hello_world(name: str) -> str:
    weekday = date.today().weekday()
    weekdays_tuple = ('понедельника', "вторника", "среды", "четверга", "пятницы", "субботы", "воскресенья")
    ending = 'й' if weekday in (2, 4, 5) else 'го'
    current_day = weekdays_tuple[weekday]
    return f"Привет, {name}! Хороше{ending} {current_day}!"


if __name__ == '__main__':
    app.run(debug=True)
