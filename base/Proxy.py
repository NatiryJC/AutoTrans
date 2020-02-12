#!/usr/bin/env python3

import requests
import re
from threading import Thread


class Proxy(Thread):
    def __init__(self, name, page):
        Thread.__init__(self)
        self.name = name
        self.page = page

    def run(self):
        print("Start :: "+self.name)
        Proxy.get(self.page)

    def get(page):
        '''get proxy address'''
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
        # url = 'http://www.kuaidaili.com/free/inha/'
        url = 'http://www.xicidaili.com/nn/'
        # pattern = re.compile(
        #         r'''<td data-title="IP">([0-9]*.[0-9]*.[0-9]*.[0-9]*)</td>\s*<td data-title="PORT">([0-9]*)</td>\n'''
        #         )
        pattern = re.compile(
                r'''<td>([0-9]*.[0-9]*.[0-9]*.[0-9]*)</td>\s*<td>([0-9]*)</td>\n'''
                )
        try:
            html = requests.get(url+str(page)+'/', headers=headers).text
            results = pattern.findall(html)
            for item in results:
                proxy_pre = item[0]+':'+item[1]
                proxies_pre = {
                        "http": "http://"+proxy_pre,
                        "https": "https://"+proxy_pre
                        }
                if Proxy.fetch(proxies_pre):
                    with open(".proxy", "a") as f:
                        f.write(proxy_pre+"\n")
        except Exception:
            pass

    def fetch(proxies=None):
        '''proxy validity verification'''
        try:
            requests.get('http://httpbin.org/get', proxies=proxies, timeout=1)
            return True
        except Exception:
            return False

    def update():
        with open(".proxy", "w") as f:
            f.write("")
        threads = []
        for page in range(1, 3):
            threads.append(Proxy("Getting in page "+str(page), page))
        for page in range(1, 3):
            threads[page-1].start()
        for page in range(1, 3):
            threads[page-1].join()

    def getinfile():
        with open(".proxy", "r") as f:
            items = f.read().split("\n")
        for proxies in items:
            proxies = {
                    "http": "http://"+proxies,
                    "https": "https://"+proxies
                    }
            if Proxy.fetch(proxies):
                return proxies

    def use(is_proxy):
        if is_proxy:
            proxies = Proxy.getinfile()
            if proxies is None:
                flag = input(":: Start Update Proxy [Y/n]")
                if flag == 'n':
                    proxies = None
                else:
                    Proxy.update()
                    proxies = Proxy.getinfile()
        else:
            proxies = None
        return proxies
