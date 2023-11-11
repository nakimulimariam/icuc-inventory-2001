from django.shortcuts import render

def index_view(request):
    return render(request, 'index.html')

def blog_list_view(request):
    return render(request, 'blog_list.html')
