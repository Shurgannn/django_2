import csv
from pprint import pprint

from django.shortcuts import render

def inflation_view(request):
    template_name = 'inflation.html'

    data_list = []
    dict_keys = ''

    # чтение csv-файла и заполнение контекста
    with open('inflation_russia.csv', encoding='utf-8', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            data_dict = {'Год': row['Год'], 'Янв': row['Янв'], 'Фев': row['Фев'], 'Мар': row['Мар'], 'Апр': row['Апр'], 'Май': row['Май'], 'Июн': row['Июн'], 'Июл': row['Июл'], 'Авг': row['Авг'], 'Сен': row['Сен'], 'Окт': row['Окт'], 'Ноя': row['Ноя'], 'Дек': row['Дек'], 'Всего': row['Суммарная']}
            dict_keys = data_dict.keys()
            data_list.append(data_dict)
    # pprint(data_list)
    pprint(dict_keys)
    context = {'data': data_list,
               'list': dict_keys}

    return render(request, template_name, context)