from django.shortcuts import render

def about(request):
    return render(request, 'aboutus/about.html')
