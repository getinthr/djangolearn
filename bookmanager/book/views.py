from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'name':'hello'
    }
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'book/index.html',context=context)