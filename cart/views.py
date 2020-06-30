from django.shortcuts import render, HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def add_item(request):
    if request.method == 'POST':
        session = request.session
        postdate = request.POST
        print(postdate)
        session[settings.CART_SESSION_ID] = postdate
    return HttpResponse('HE')


@csrf_exempt
def index(request):
    session = request.session
    hhm = session[settings.CART_SESSION_ID]
    print(hhm)
    return HttpResponse('he')
