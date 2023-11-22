from django.shortcuts import render

# Create your views here.

def person1(request):
    return render(request, 'person1.html')


def person2(request):
    return render(request, 'person2.html')


def p1reply(request):
    return render(request, 'p1reply.html')