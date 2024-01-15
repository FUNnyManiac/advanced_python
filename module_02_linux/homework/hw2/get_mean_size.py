"""
Удобно направлять результат выполнения команды напрямую в программу с помощью конвейера (pipe):

$ ls -l | python3 get_mean_size.py

Напишите функцию get_mean_size, которая на вход принимает результат выполнения команды ls -l,
а возвращает средний размер файла в каталоге.
"""

import sys


def get_mean_size(ls_output: str) -> float:
    total_size = 0
    count = 0
    for line in ls_output:
        count += 1
        total_size += float(line.split()[4])
    return total_size / count


if __name__ == '__main__':
    data: list = sys.stdin.readlines()[1:]
    if not data:
        print("Directory is empty")
    else:
        mean_size: float = get_mean_size(data)
        print(f'Mean size of file in current directory: {mean_size} byte')