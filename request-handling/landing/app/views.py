from collections import Counter

from django.http import HttpResponse
from django.shortcuts import render_to_response

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()



def index(request):
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    from_landing = request.GET.get('from-landing')
    if from_landing == 'original':
        counter_click['original'] += 1
    elif from_landing == 'test':
        counter_click['test'] += 1
    original_counter_click = counter_click['original']
    test_counter_click = counter_click['test']
    print(counter_click, original_counter_click, test_counter_click)
    return render_to_response('index.html')

def landing(request):
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов
    view = request.GET.get('ab-test-arg')
    landing_req = 'landing.html'
    if view == 'original':
        landing_req = 'landing.html'
        counter_show['original'] +=1
    elif view == 'test':
        landing_req = 'landing_alternate.html'
        counter_show['test'] += 1
    original_counter_show = counter_show['original']
    test_counter_show = counter_show['test']
    print(counter_show, 'original_counter_show = ' + str(original_counter_show), 'test_counter_show =' + str(test_counter_show))
    return render_to_response(landing_req)
#
#
def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Чтобы отличить с какой версии лендинга был переход
    # проверяйте GET параметр marker который может принимать значения test и original
    # Для вывода результат передайте в следующем формате:
    original_ratio_original = counter_click['original'] / counter_show['original']
    test_ratio_original = counter_click['test'] / counter_show['test']
    return render_to_response('stats.html', context={
        'test_conversion': test_ratio_original,
        'original_conversion': original_ratio_original,
    })
