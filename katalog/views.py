from django.shortcuts import render

def index(request):
    context = {
        'nama': 'Hello World',
    }
    return render(request, 'index.html', context)