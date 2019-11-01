from django import template

register = template.Library()


@register.filter
def fun(dic: dict, key: str = '') -> float:
    return dic[key]
