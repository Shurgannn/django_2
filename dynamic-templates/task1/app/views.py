import csv
from pprint import pprint

from django.shortcuts import render

def inflation_view(request):
    template_name = 'inflation.html'
    d_keys = ''
    data_list = []
    # чтение csv-файла и заполнение контекста
    with open('inflation_russia.csv', encoding='utf-8', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            data_dict = {'Год': row['Год'], 'Янв': row['Янв'], 'Фев': row['Фев'], 'Мар': row['Мар'],
                         'Апр': row['Апр'], 'Май': row['Май'], 'Июн': row['Июн'], 'Июл': row['Июл'],
                         'Авг': row['Авг'], 'Сен': row['Сен'], 'Окт': row['Окт'], 'Ноя': row['Ноя'],
                         'Дек': row['Дек'], 'Всего': row['Суммарная']}
            d_keys = data_dict.keys()
            print(d_keys)
            for k, v in data_dict.items():
                if v == '':
                    data_dict[k] = 0
                else:
                    if k == 'Год':
                        data_dict[k] = int(v)
                    else:
                        data_dict[k] = float(v)
            data_list.append(data_dict)
    context = {'data': data_list,
               'list_k': d_keys}

    return render(request, template_name, context)
