# -*- coding=utf-8 -*-
import requests
from bs4 import BeautifulSoup as bs

def IP(ip):
    response = requests.get('http://www.hao7188.com/ip/%s.html'%ip).content
    soup = bs(response, 'html.parser')
    c = soup.findAll('img',align='absmiddle')
    b = [item.string for item in c if item.string ]
    return "\n".join(b)

def BanWaGong(location):
    pass



