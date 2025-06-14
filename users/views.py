from django.shortcuts import render , HttpResponse


def members(request):
    context = {
        'myname':'omkar'
    }
    return render(request , 'users/index.html' , context)
