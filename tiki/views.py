from django.http import HttpResponse
from time import strftime

def index(request):
    current_time = strftime('%Y-%m-%d %H:%M:%S')
    return HttpResponse('Hello World! <br/> Now=' + str(current_time))

