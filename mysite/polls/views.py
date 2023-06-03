from django.http import HttpResponse


def index(request):
    return HttpResponse('''{"message":"Hello Zamon. It is your first Django app"}''')


def index1(request):
    return HttpResponse("Ko'nglimaaaa, ko'nglimaaaa, ko'ngliiiiiimmmmmmmmm")