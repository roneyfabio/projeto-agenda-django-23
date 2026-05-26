from django.http import Http404  # noqa: F401
from django.shortcuts import render

from contact.models import Contact  # noqa: F401


def create(request):
    
    context = {}

    return render(
        request,
        'contact/create.html',
        context
    )
