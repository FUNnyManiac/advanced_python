"""
Реализуйте приложение для учёта финансов, умеющее запоминать, сколько денег было потрачено за день,
а также показывать затраты за отдельный месяц и за целый год.

В программе должно быть три endpoints:

/add/<date>/<int:number> — сохранение информации о совершённой в рублях трате за какой-то день;
/calculate/<int:year> — получение суммарных трат за указанный год;
/calculate/<int:year>/<int:month> — получение суммарных трат за указанные год и месяц.

Дата для /add/ передаётся в формате YYYYMMDD, где YYYY — год, MM — месяц (от 1 до 12), DD — число (от 01 до 31).
Гарантируется, что переданная дата имеет такой формат и она корректна (никаких 31 февраля).
"""
import datetime

from flask import Flask

app = Flask(__name__)

storage = {}
months = ("january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november",
          "december",)


@app.route("/add/<date>/<int:number>")
def add(date: str, number: int):
    year = int(date[:4])
    month = int(date[4:6])
    day = int(date[6:])
    try:
        datetime.date(year, month, day)
        storage.setdefault(year, {}).setdefault(month, 0)
        storage[year][month] += number
    except ValueError:
        return f"Please write correct date!"
    return f"Added! {storage}"


@app.route("/calculate/<int:year>")
def calculate_year(year: int):
    total_sum = 0
    try:
        for sum in storage[year].values():
            total_sum += sum
        return f"Expenses for the {year} year: {total_sum}"
    except KeyError:
        return f"No data for the {year} year!"


@app.route("/calculate/<int:year>/<int:month>")
def calculate_month(year: int, month: int):
    try:
        return f"Expenses for the {months[month]} in {year} year: {storage[year][month]}"
    except KeyError:
        return f"No data for the {months[month]} in {year} year!"


if __name__ == "__main__":
    app.run(debug=True)
