from django.shortcuts import render

# Create your views here.
def blog(request):
    return render(request, 'blog.html')

def single_blog(request):
    return render(request, 'single-blog.html')
