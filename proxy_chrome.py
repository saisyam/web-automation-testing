from splinter import Browser
from selenium import webdriver
from getproxies import GetProxies

gp = GetProxies()
proxies = gp.get_proxies('https', 'DE')
url = "https://www.expressvpn.com/what-is-my-ip"

for proxy in proxies:
    PROXY = proxy['ip']+":"+proxy['port']
    print("Proxy: "+ PROXY)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=%s' % PROXY)
    chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36')
    try:
        browser = Browser('chrome', options=chrome_options)
        browser.visit(url)
        ip_address = browser.find_by_css('p[class="ip-address"').text
        if ip_address == proxy['ip']:
            print("IP address match with Proxy: "+ip_address)
            browser.quit()
            break    
    except Exception as e:
        browser.quit()
        print("Trying another proxy....")
        continue
