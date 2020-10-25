from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def home_view(request):
    #return HttpResponse('Hello WOrld!!')
    user = request.user
    hello = 'Hello World'

    context = {
        'user': user,
        'hello': hello,
    }
    
    return render(request, 'main/home.html', context)



