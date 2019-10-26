from datetime import datetime, date
import os
from pprint import pprint

from django.shortcuts import render, render_to_response

from app.settings import FILES_PATH


def file_list(request, date:datetime=None):
    template_name = 'index.html'
    dirs = os.listdir(FILES_PATH)
    data_list = []
    context = {}
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    for file in dirs:
        file_stats = os.stat(os.path.join(FILES_PATH, file))
        ctime = datetime.fromtimestamp(file_stats.st_ctime).date()
        mtime = datetime.fromtimestamp(file_stats.st_mtime).date()
        data_dict = {'name': file,
                     'ctime': ctime,
                     'mtime': mtime}
        if date != None:
            if date.date() == ctime:
                data_list.append(data_dict)
            context['date'] = date.date()
        else:
            data_list.append(data_dict)
    context['files'] = data_list
    return render(request, template_name, context)


def file_content(request, name):
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    dirs = os.listdir(FILES_PATH)
    if name in dirs:
        for file in dirs:
            with open(f'{FILES_PATH}/{file}') as f:
                file_content = f.read()
                # print(file_content)
            context = {'file_name': name, 'file_content': file_content}
    else:
        context = {'file_name': name, 'file_content': 'Запрашиваемый файл отсутсвует'}


    return render(request, 'file_content.html', context)

