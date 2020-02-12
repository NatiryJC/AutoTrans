#!/usr/bin/env python3

import requests
import re


class proxy():
    def online(page):
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
        results = []
        try:
            html = requests.get(url+str(page)+'/', headers=headers).text
            proxies = pattern.findall(html)
            for item in proxies:
                results.append(item[0]+':'+item[1])
            return results
        except Exception:
            return results

    def fetch(proxies=None):
        '''proxy validity verification'''
        try:
            requests.get('http://httpbin.org/get', proxies=proxies, timeout=1)
            return True
        except Exception:
            return False

    def merge(item):
        return {
                "http": "http://"+item,
                "https": "https://"+item
                }

    def update():
        proxies = []
        results = ""
        for page in range(1, 2):
            proxies += proxy.online(page)
        for i in range(0, len(proxies)):
            print("\r(%d/%d)" % (i, len(proxies)), end="")
            if proxy.fetch(proxy.merge(proxies[i])):
                print("\tavailable", end="")
                results += str(proxies[i])+"\n"
            else:
                print("\tunavailable", end="")
        with open(".proxy", "w") as f:
            f.write(results)

    def local():
        with open(".proxy", "r") as f:
            proxies = f.read().splitlines()
        for i in range(0, len(proxies)):
            print("\rTry # %d:" % i, end="")
            if proxy.fetch(proxy.merge(proxies[i])):
                print("\tavailable", end="")
                return proxies[i]
            else:
                print("\tunavailable", end="")

    def run(is_proxy):
        if is_proxy:
            print(":: Try to get proxy ...")
            proxies = proxy.local()
            print()
            if proxies is None:
                flag = input(":: Start Update Proxy [Y/n]")
                if flag == 'n':
                    print(":: No proxy")
                    proxies = None
                else:
                    proxy.update()
                    print(":: Try to get proxy again ...")
                    proxies = proxy.local()
                    print()
        else:
            print(":: No proxy")
            proxies = None
        return proxies
