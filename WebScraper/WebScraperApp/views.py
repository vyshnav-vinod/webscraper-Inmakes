from django.shortcuts import render, redirect
from .models import Links

from bs4 import BeautifulSoup
import requests
# Create your views here.


def index(request):
    if request.method == 'POST':
        postlink = request.POST.get('linkname', '')
        url = requests.get(postlink)
        bs = BeautifulSoup(url.text, 'html.parser')
        for link in bs.find_all('a'):
            link_addr = link.get('href')
            link_name = link.string
            Links.objects.create(name=link_name, address=link_addr)
        return redirect('/')
    data = Links.objects.all()
    return render(request, 'index.html', {'links': data})
