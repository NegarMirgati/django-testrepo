from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author' : 'Negar Mirgati',
        'title' : 'blog post 1',
        'content' : 'bye bye bye',
        'date' : 'August 28, 2019'
    }
    ,
    {
        'author' : 'Mehrdad Nourbakhsh',
        'title' : 'blog post 2',
        'content' : 'hi hi hi',
        'date' : 'August 29, 2019'
    }
]

def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context )

def about(request):
    return render(request, 'blog/about.html', {'title' : 'About'})
