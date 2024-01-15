"""
С помощью команды ps можно посмотреть список запущенных процессов.
С флагами aux эта команда выведет информацию обо всех процессах, запущенных в системе.

Запустите эту команду и сохраните выданный результат в файл:

$ ps aux > output_file.txt

Столбец RSS показывает информацию о потребляемой памяти в байтах.

Напишите функцию get_summary_rss, которая на вход принимает путь до файла с результатом выполнения команды ps aux,
а возвращает суммарный объём потребляемой памяти в человекочитаемом формате.
Это означает, что ответ надо перевести в байты, килобайты, мегабайты и так далее.
"""
import os

def get_summary_rss(ps_output_file_path: str) -> str:
    process_list_cmd = 'ps aux > {}'.format(ps_output_file_path)
    os.system(process_list_cmd)
    total_RSS = 0
    with open(ps_output_file_path) as data:
        for line in data.readlines()[1:]:
            curr_process_rss = int(line.split()[5])
            total_RSS += curr_process_rss

    labels = {0: 'кило', 1: 'мега', 2: 'гига', 3: 'тера'}
    label = 0
    while total_RSS > 1024:
        total_RSS /= 1024
        label += 1

    return f"Total RSS {round(total_RSS, 3)} {labels[label]}байт"


if __name__ == '__main__':
    path: str = 'test.txt'
    summary_rss: str = get_summary_rss(path)
    print(summary_rss)
