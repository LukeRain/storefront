from django.shortcuts import render
from django.http import HttpResponse


# A view function is a request handler (in: request, out: response)
def say_hello(request):
    """
    Basic example of a view function
    :param request:
    :return:
    """
    x = 1
    y = 2
    return render(request, 'hello.html', {'name': 'Luc'})

