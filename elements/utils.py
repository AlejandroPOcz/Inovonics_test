# Django
from django.http import HttpResponse
from django.shortcuts import redirect

# Models
from .models import Element


def home_view(request):
    message = """
    Hello! and welcome to the home page of this project.\n
    This is a simple list manager of integers (we can only manage integers).\n
    Here are the different paths you can access and how to use them:\n
    \n
    1.- /elements/\n
    This Display us the elements that we actually have in our database


    """

    return HttpResponse(message)


def elements(request):
    elements = Element.objects.all().order_by("order")
    return HttpResponse(elements)


def add_beginning(request, num):
    if Element.objects.all().exists():
        current = Element.objects.all().order_by("order").last().order
        while True:
            element = Element.objects.get(order=current)
            element.order = current+1
            element.save()
            current -= 1
            if current == 0:
                break
    new_element = Element(content=num, order=1)
    new_element.save()
    response = redirect('/elements/')
    return response


def add_end(request, num):
    if Element.objects.all().exists():
        last = Element.objects.all().order_by("order").last().order
        new_element = Element(content=num, order=last+1)
        new_element.save()
    else:
        new_element = Element(content=num, order=1)
        new_element.save()
    response = redirect('/elements/')
    return response


def add_before(request, old_num, new_num):
    if Element.objects.filter(content=old_num).exists():
        objective = Element.objects.filter(content=old_num)[0].order
        current = Element.objects.all().order_by("order").last().order
        while True:
            element = Element.objects.get(order=current)
            element.order = current+1
            element.save()
            current -= 1
            if current == objective-1:
                break
        new_element = Element(content=new_num, order=objective)
        new_element.save()
        response = redirect('/elements/')
        return response
    else:
        return HttpResponse("The number you typed is not in the list.")


def add_after(request, old_num, new_num):
    if Element.objects.filter(content=old_num).exists():
        objective = Element.objects.filter(content=old_num)[0].order
        current = Element.objects.all().order_by("order").last().order
        while True:
            element = Element.objects.get(order=current)
            element.order = current+1
            element.save()
            current -= 1
            if current == objective:
                break
        new_element = Element(content=new_num, order=objective+1)
        new_element.save()
        response = redirect('/elements/')
        return response
    else:
        return HttpResponse("The number you typed is not in the list.")


def index(request, num):
    if Element.objects.filter(content=num).exists():
        order = Element.objects.filter(content=num)[0].order
        return HttpResponse(f"The number you typed has the index: {order}")
    else:
        return HttpResponse("The number you typed is not in the list.")
