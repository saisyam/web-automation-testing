from bs4 import BeautifulSoup
import requests
from lxml import html

def get_ssl_proxies():
    proxies = []
    response = requests.get("https://sslproxies.org/", timeout=15)
    tree = html.fromstring(response.text)
    for tr in tree.xpath("//table[@id='proxylisttable']/tbody/tr"):
        ip = tr.xpath(".//td[1]/text()")
        port = tr.xpath(".//td[2]/text()")
        if len(ip) > 0 and len(port) > 0:
            proxies.append(ip[0]+":"+port[0])
    return proxies

def get_free_proxies():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = html.fromstring(response.text)
    proxies = []
    for i in parser.xpath('//tbody/tr')[:20]:
        #if i.xpath('.//td[7][contains(text(),"yes")]'):
        proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
        proxies.append(proxy)
    return proxies

def get_proxies():
    url = "https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all&ssl=all&anonymity=all"
    resp = requests.get(url)
    proxies = resp.text.split("\r\n")
    return proxies[:-1]