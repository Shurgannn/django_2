from pprint import pprint

from django.db.models.functions import math
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv

from app.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    data_list = []
    with open(BUS_STATION_CSV, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data_dict = {'Name': row['Name'], 'Street': row['Street'], 'District': row['District']}
            data_list.append(data_dict)

    # current_page = int(request.GET.get('page', 1))
    # items_per_page = 7
    # total_pages = int(len(data_list) / items_per_page)
    # if current_page <= 0:
    #     current_page = 1
    # if current_page > total_pages:
    #     current_page = total_pages
    # data = data_list[(current_page - 1) * items_per_page: current_page * items_per_page]

    current_page = int(request.GET.get('page', 1))
    items_per_page = 7

    paginator = Paginator(data_list, items_per_page)
    page = paginator.get_page(current_page)
    data = page.object_list

    if page.has_next():
        next_page_url = f'?page={page.next_page_number()}'
    else:
        next_page_url = None
    if page.has_previous():
        prev_page_url = f'?page={page.previous_page_number()}'
    else:
        prev_page_url = None

    return render_to_response('index.html', context={
        'bus_stations': data,
        'current_page': current_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    })
