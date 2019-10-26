from django.urls import path, register_converter

# Определите и зарегистрируйте конвертер для определения даты в урлах и наоборот урла по датам
from app.path_converter import DateConverter
from app.views import file_list, file_content

register_converter(DateConverter, 'date_conv')

urlpatterns = [
    # Определите схему урлов с привязкой к отображениям .views.file_list и .views.file_content
    path('', file_list, name='file_list'),
    path('<date_conv: date>/', file_list, name='file_date_list'),    # задайте необязательный параметр "date"
                                      # для детальной информации смотрите HTML-шаблоны в директории templates
    path('file/<name>/', file_content, name='file_content'),
]
