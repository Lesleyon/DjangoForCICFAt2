from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <h1>Хеллоу Ворлд</h1>
        <p>Тестовое Сообщение</p>
    """)