from splinter import Browser
from selenium import webdriver
from getproxies import GetProxies
from useragent import UserAgent

gp = GetProxies()
proxies = gp.get_proxies('https', 'DE')
url = "https://www.expressvpn.com/what-is-my-ip"

for proxy in proxies:
    print("Proxy: "+ proxy)
    ua = UserAgent()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=%s' % proxy)
    chrome_options.add_argument('user-agent='+ua.get_user_agent("chrome"))
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
