# This class provies a list of HTTP/HTTPS proxies based on country code
# This proxy API is taken from https://www.proxy-list.download/api/v1

import requests
import json

class GetProxies:
    def __init__(self):
        self.url = "https://www.proxy-list.download/api/v1/get"
        self.getproxylisturl = "https://api.getproxylist.com/proxy"
        self.proxyscrapeurl = "https://api.proxyscrape.com"
        
    def get_proxies(self, type, country):
        url = self.url+"?type="+type+"&country="+country+"&anon=elite"
        r = requests.get(url)
        proxies = []
        if r.status_code == 200:
            response = r.text.split("\r\n")
            for line in response:
                proxy = {}
                data = line.split(":")
                if len(data) == 2:
                    proxy["ip"] = data[0]
                    proxy["port"] = data[1]
                    proxies.append(proxy)
            return proxies
        else:
            return None
    
    def getproxylist(self, type, country):
        url = self.getproxylisturl+"?anonymity[]=high%20anonymity&anonymity[]=transparent&maxConnectTime=1&country[]="+country
        if type=="https":
            url = url + "&allowHttps=1"
        r = requests.get(url)
        proxies = []
        if r.status_code == 200:
            proxy = {}
            proxy_data = json.loads(r.text)
            proxy["ip"] = proxy_data['ip']
            proxy["port"] = proxy_data['port']
            proxies.append(proxy)
            return proxies
        else:
            return None
    
    def proxyscrape(self, type, country):
        url = self.proxyscrapeurl+"?request=getproxies&proxytype=http&timeout=5000&anonymity=elite&country="+country
        if type=="https":
            url = url + "&ssl=yes"
        r = requests.get(url)
        proxies = []
        if r.status_code == 200:
            response = r.text.split("\r\n")
            for line in response:
                proxy = {}
                data = line.split(":")
                if len(data) == 2:
                    proxy["ip"] = data[0]
                    proxy["port"] = data[1]
                    proxies.append(proxy)
            return proxies
        else:
            return None

'''
gp = GetProxies()
proxies = gp.proxyscrape('https', 'DE')
print(proxies)
'''