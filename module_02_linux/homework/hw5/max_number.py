"""
Реализуйте endpoint, начинающийся с /max_number, в который можно передать список чисел, разделённых слешем /.
Endpoint должен вернуть текст «Максимальное переданное число {number}»,
где number — выделенное курсивом наибольшее из переданных чисел.

Примеры:

/max_number/10/2/9/1
Максимальное число: 10

/max_number/1/1/1/1/1/1/1/2
Максимальное число: 2

"""

from flask import Flask

app = Flask(__name__)


@app.route("/max_number/<path:numbers>")
def max_number(numbers):
    try:
        int_numbers = [int(number) for number in numbers.split('/')]
        max_number = max(int_numbers)
    except ValueError:
        return "Должны быть только целые числа!"

    return f"Максимальное число из чисел <i>{int_numbers}</i> = <b>{max_number}</b>"


if __name__ == "__main__":
    app.run(debug=True)
