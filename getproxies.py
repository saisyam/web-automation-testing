import requests
import json
import random

class GetProxies:
    def __init__(self):
        self.url = "https://www.proxy-list.download/api/v1/get"
        self.getproxylisturl = "https://api.getproxylist.com/proxy"
        self.proxyscrapeurl = "https://api.proxyscrape.com"
        
    def getfreeproxies(self, type, country, port=None):
        choice = random.randint(1,3)
        proxies = []
        if choice == 1:
            proxies = self.get_proxies(type, country, port)
        elif choice == 2:
            proxies = self.getproxylist(type, country, port)
        elif choice == 3:
            proxies =  self.proxyscrape(type, country, port)
        
        if proxies is None and choice == 1:
            proxies = self.getproxylist(type, country, port)
        if proxies is None and choice == 2:
            proxies = self.proxyscrape(type, country, port)
        if proxies is None and choice == 3:
            proxies = self.get_proxies(type, country, port)

        return proxies

    def get_proxies(self, type, country, port=None):
        url = self.url+"?type="+type+"&country="+country+"&anon=elite"
        r = requests.get(url)
        proxies = []
        if r.status_code == 200:
            response = r.text.split("\r\n")
            for line in response:
                data = line.split(":")
                if len(data) == 2:
                    if port == None:
                        proxies.append(data[0]+":"+data[1])
                    if port is not None and port == data[1]:
                        proxies.append(data[0]+":"+data[1])
            return proxies
        else:
            return None

    # Not an effective proxy provider 
    def getproxylist(self, type, country, port=None):
        url = self.getproxylisturl+"?anonymity[]=high%20anonymity&anonymity[]=transparent&maxConnectTime=1&country[]="+country
        if type=="https":
            url = url + "&allowHttps=1"
        r = requests.get(url)
        proxies = []
        if r.status_code == 200:
            proxy_data = json.loads(r.text)
            if port == None:
                proxies.append(proxy_data['ip']+":"+str(proxy_data['port']))
            if port is not None and port == proxy_data['port']:
                proxies.append(proxy_data['ip']+":"+str(proxy_data['port']))
            return proxies
        else:
            return None
    
    def proxyscrape(self, type, country, port=None):
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
                    if port == None:
                        proxies.append(data[0]+":"+data[1])                        
                    if port is not None and port == data[1]:
                        proxies.append(data[0]+":"+data[1])
            return proxies
        else:
            return None

'''
gp = GetProxies()
proxies = gp.getproxylist('https', 'US')
print(proxies)
'''