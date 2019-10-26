from datetime import datetime, date
import os
from pprint import pprint

from django.shortcuts import render, render_to_response

from app.settings import FILES_PATH


def file_list(request, date=None):
    template_name = 'index.html'
    dirs = os.listdir(FILES_PATH)
    statinfo = os.stat(FILES_PATH)
    for i in statinfo:
        print(i)
    data_list = []
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    for file in dirs:
        data_dict = {'name': file,
                     'ctime': statinfo[9],
                     'mtime': statinfo[8]}
        data_list.append(data_dict)
    # pprint(data_list)

    context = {'files': data_list,
               'date': date}  # Этот параметр необязательный

    return render(request, template_name, context)


def file_content(request, name):
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    dirs = os.listdir(FILES_PATH)
    if name in dirs:
        for file in dirs:
            with open(f'C:/My documents/Django_1/dj-homeworks/request-handling/file_server/files/{file}', encoding='utf-8') as f:
                file_content = f.read()
                print(file_content)
            context = {'file_name': name, 'file_content': file_content}
    else:
        context = {'file_name': 'file_name_1.txt', 'file_content': 'File content!'}


    return render(request, 'file_content.html', context)

