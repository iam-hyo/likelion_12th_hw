from django.shortcuts import render

# Create your views here.

def mainpage(request):
    context = {
        'MTV': ['Model', 'Template', 'Views']
        }  
    return render(request, 'main/mainpage.html', context)

def secondpage(request):
    return render(request, 'main/secondpage.html')