from django.http import HttpResponse
from django.shortcuts import render

from burgers.models import Burger


def main(request):
    # return HttpResponse("Hello, world. You're at the helloworld main page.")
    return render(request, 'main.html')

def lunchlist(request):
    # return HttpResponse("lunch list : 점심 메뉴 입니다!")
    return render(request, 'lunchlist.html')
def introduce(request):
    return  HttpResponse("안녕하세요 저는 조이한 입니다. 잘 부탁드립니다!")

def burger_list(request):
    burgers = Burger.objects.all()
    print("햄버거 전체 목록", burgers)
    context = {'burgers': burgers}
    return render(request, 'burger_list.html',context)