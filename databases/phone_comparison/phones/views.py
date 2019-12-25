import csv

from django.shortcuts import render
from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    data_list = []
    with open('phones.csv', encoding='utf-8', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            data_dict = {'Название': row['name'], 'Цена': row['price'], 'Операционнаясистема': row['operating_system']}
            d_keys = data_dict.keys()
            print(d_keys)
    # data = csv.reader(open('phones.csv'), delimiter=';')
    # for row in data:
    #     if row[0] != 'id':
    #         phone = Phone()
    #         phone.id = row[0]
    #         phone.name = row[1]
    #         phone.operating_system = row[3]
    #         phone.price = row[2]
    #         phone.save()
    # serv_list = Phone.objects.all()
            data_list.append(data_dict)
    print(data_list)
    context = {'data': data_list,
               'list_k': d_keys}
    return render(
        request,
        template,
        context
    )
