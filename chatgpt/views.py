from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def one_func(request):
    return render(request, "index.html")

def t_fun(request):
    data_in = request.GET['a']
    with open("./chatgpt/data.txt",'w') as ff:
        ff.write(data_in)
    return HttpResponse("<center><h1>saved data</h1><center>")

def y_fun(request):
    with open("./chatgpt/data.txt",'r') as ff:
        data_out = ff.read()
    codes = "<textarea rows=100 cols=100>"+data_out+"</textarea>"
    return HttpResponse(codes)

