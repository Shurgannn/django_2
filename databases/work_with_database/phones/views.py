from django.shortcuts import render, render_to_response

from phones.models import Phone


def index(request):
    return render_to_response('base.html')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    serv_list = Phone.objects.all()
    if sort == 'name':
       serv_list = Phone.objects.order_by('name')
    elif sort == 'price':
       serv_list = Phone.objects.order_by('price')
    elif sort == 'price-':
       serv_list = Phone.objects.order_by('-price')
    context = {'serv_list': serv_list,
               'sort_list': sort}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    serv_list = Phone.objects.filter(slug=slug)
    # for a in serv_list:
    #     print(a.name)
    context = {'serv_list': serv_list}
    return render(request, template, context)
