#!/usr/bin/env python3

import requests
import re
from threading import Thread


class proxy(Thread):
    def __init__(self, name, page):
        Thread.__init__(self)
        self.name = name
        self.page = page

    def run(self):
        print("Start :: "+self.name)
        proxy.proxy_get(self.page, self.name)

    def proxy_get(page, name):
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
                if proxy.proxy_fetch(name, proxies_pre):
                    with open(".proxy", "a") as f:
                        f.write(proxy_pre+"\n")
        except Exception:
            pass

    def proxy_fetch(name, proxies):
        '''proxy validity verification'''
        try:
            requests.get('http://httpbin.org/get', proxies=proxies, timeout=1)
            print(name, "True")
            return True
        except Exception:
            print(name, "False")
            return False


with open(".proxy", "w") as f:
    f.write("")
threads = []
for page in range(1, 5):
    threads.append(proxy("Getting in page "+str(page), page))
for page in range(1, 5):
    threads[page-1].start()
