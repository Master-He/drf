from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.core.urlresolvers import reverse


def index(request):
    """

    Args:
        request:

    Returns:

    """
    response = HttpResponse("hello world!")
    response.status_code = 200
    response.set_cookie('A', "1", max_age=300)
    return response


def say(request):
    A = request.COOKIES.get("A", "123")
    print(A)
    print(type(A))
    url = reverse('users:index')
    return HttpResponse(url)


def header(request):
    return redirect(reverse('users:index'))
