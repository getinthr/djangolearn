from django.http import HttpResponse
from django.shortcuts import render, redirect

from book.models import BookInfo


# Create your views here.
def create_book(request):

    book =BookInfo.objects.create(
        name='abc',
        pub_date='2000-01-01',
        readcount=10
    )
    return HttpResponse('create')

def shop(request,city_id,mobile):
    # import re
    # if not re.match('\d{5}',shop_id):
    #     return HttpResponse('shop_id is not valid')
    # query_params = request.GET

    return HttpResponse('shop')

def register(request):
    data = request.POST
    print(data)
    return HttpResponse('register')

def json(request):
    body=request.body
    body_str = request.body.decode('utf-8')
    print(body_str)
    return HttpResponse('json')

def method(request):
    print(request.method)
    return HttpResponse('method')

from django.http import JsonResponse,HttpResponse
def response(request):

    # reponse=HttpResponse('response',status=200)
    # reponse['name']='itcast'
    # return reponse

    info={
        'name':'itcast',
        'age':18
    }
    girl_firends = [
        {
        'name': 'rose',
        'age': 18
        },
        {
            'name': 'jack',
            'age': 20
        }
    ]
    # response=JsonResponse(data=girl_firends,safe=False)
    # return response
    return redirect('http://www.baidu.com')