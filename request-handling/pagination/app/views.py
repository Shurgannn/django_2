from pprint import pprint

from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv

from app.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    data_dict = {}
    with open(BUS_STATION_CSV, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # data = (row['Name'], row['Street'], row['District'])
            data_dict['Name'], data_dict['Street'], data_dict['District'] = (row['Name']), (row['Street']), (row['District'])
    print(len(data_dict))
    pprint(data_dict)

    current_page = 1
    next_page_url = 'write your url'
    return render_to_response('index.html', context={
        'bus_stations': [{'Name': data_dict['Name'], 'Street': data_dict['Street'], 'District': data_dict['District']}],
        'current_page': current_page,
        'prev_page_url': None,
        'next_page_url': next_page_url,
    })


# DATA = [str(i + 1) for i in range(100)]
#
# def pag_view(request):
#     page_num = int(request.GET.get('page', 1))
#     count = 7
#
#     paginator = Paginator(DATA, count)
#     page = paginator.get_page(page_num)
#     data = page.object_list
#
#     print(page.number)
#     if page.has_next():
#         print('next = ', page.next_page_number())
#     if page.has_previous():
#         print('previous = ', page.previous_page_number())
#
#     msg = '<br>'.join(data)
#     return HttpResponse(msg)

