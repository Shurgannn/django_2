from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    context = {'object_list': Student.objects.all()}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'

    return render(request, template, context)

# {% for student in object_list %}
#     <li>{{ student.name }} {{ student.group }}
#
#       {% for obj_teacher in object.teachers.all %}
#     <p>{{ obj_teacher.name }}  {{ obj_teacher.subject }}</p>
#       {% endfor %}
#       <br> Преподаватель: {{ student.teacher.name }} {{ student.teacher.subject }}</li>
#   {% endfor %}
