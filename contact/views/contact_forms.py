from django.http import Http404  # noqa: F401
from django.shortcuts import render

from contact.models import Contact  # noqa: F401


def create(request):
    if request.method =='POST':
        print()
        print(request.method)
        print(request.POST.get('first_name'))
        print(request.POST.get('last_name'))
        print()        
    
    
    
    
    context = {}

    return render(
        request,
        'contact/create.html',
        context
    )
