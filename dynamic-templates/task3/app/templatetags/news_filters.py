from datetime import datetime, date

from django import template

from app.views import do_request

register = template.Library()


@register.filter
def format_date(value):#: datetime) -> int:
    # Ваш код
    date = datetime.fromtimestamp(value)
    now = datetime.now()
    delta = (now - date).total_seconds()
    if delta < 600:
        post_date = 'только что'
    elif 600 <= delta <= 86400:
        if 600 <= delta < 3600:
           delta_min = int(delta // 60)
           post_date = f'{delta_min} минут назад'
        else:
            delta_hour = int(delta // 3600)
            post_date = f'{delta_hour} часов назад'
    else:
        post_date = date
    return post_date


# необходимо добавить фильтр для поля `score`
@register.filter
def format_score(value: int = 0) -> str:
    if value < -5:
        post_value = 'все плохо'
    elif -5 <= value <= 5:
        post_value = 'нейтрально'
    else:
        post_value = 'хорошо'
    return post_value

@register.filter
def format_num_comments(value: int) -> str or int:
    # Ваш код
    if value == 0:
        post_num_comments = 'Оставьте комментарий'
    elif 0 < value <= 50:
        post_num_comments = value
    else:
        post_num_comments = '50+'
    return post_num_comments

@register.filter
def format_selftext(value: str, count: int = 5) -> str:
    post_format_selftext_first = ''
    post_format_selftext_last = ''
    post_format_selftext = ''
    e = value.split()
    if 0 < len(e) < count * 2:
        for i in e:
            post_format_selftext += i
    elif len(e) == 0:
        post_format_selftext = ''
    else:
        b = e[0:count]
        c = e[-count:]
        for i in range(count):
            post_format_selftext_first += ' ' + b[i]
            post_format_selftext_last += ' ' + c[i]
        post_format_selftext = post_format_selftext_first + ' ... ' + post_format_selftext_last
    return post_format_selftext

