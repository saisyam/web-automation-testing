# This class provies a list of HTTP/HTTPS proxies based on country code
# This proxy API is taken from https://www.proxy-list.download/api/v1

import requests

class GetProxies:
    def __init__(self):
        self.url = "https://www.proxy-list.download/api/v1/get"
        
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


gp = GetProxies()
proxies = gp.get_proxies('https', 'DE')
print(proxies)