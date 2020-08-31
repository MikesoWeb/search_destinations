from datetime import datetime

def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')

def clear(line):
    clear_line = line.strip().split(',')
    return clear_line

def search_destination(b, flights_reverse):
    for i in [i[b] for i in flights_reverse if b in i]:
        print(f'{i} отправление в {b}')

def all_destinations(flights_reverse):
    for i in flights_reverse:
        for j, k in i.items():
            print(f'{j} - {k}')

def open_csv_and_result(b=''):
    with open('data_children.csv') as data:
        ignore_line = data.readline()
        flights_reader_and_clear = dict(clear(dirty_line) for dirty_line in data)
        flights_sorted = dict(sorted({convert2ampm(k), v.title()}) for k, v in flights_reader_and_clear.items())
        flights_reverse = list({v: k} for k, v in flights_sorted.items())

        if b:
            search_destination(b.title(), flights_reverse)
        else:
            print('Здесь все маршруты на сегодняшний день.')
            all_destinations(flights_reverse)

open_csv_and_result('FREport')
