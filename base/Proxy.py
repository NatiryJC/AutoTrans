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
            print("\r"+" "*60+"\r\t  ( %d/%d )" % (i, len(proxies)), end="")
            if proxy.fetch(proxy.merge(proxies[i])):
                print("\tavailable", end="")
                results += str(proxies[i])+"\n"
            else:
                print("\tunavailable", end="")
        with open(".proxy", "w") as f:
            f.write(results)

    def local():
        result = None
        with open(".proxy", "r") as f:
            proxies = f.read().splitlines()
            for i in range(0, len(proxies)):
                print("\r"+" "*60, end="")
                print("\r"+" "*60+"\r\t  Try # %d:" % (i+1), end="")
                if proxy.fetch(proxy.merge(proxies[i])):
                    result = proxies[i]
                    print("\tavailable", end="")
                    break
                else:
                    print("\tunavailable", end="")
        return result

    def run():
        print("\t\u2192 Try proxy ...")
        proxies = proxy.local()
        print("\r"+" "*60, end="")
        if proxies is None:
            flag = input("\r\t\u2192 Failed. Update Proxy? [Y/n] ")
            if flag == 'n':
                print("\r"+" "*60, end="")
                print("\r\t\u2192 No proxy")
                proxies = None
            else:
                proxy.update()
                print("\r"+" "*60, end="")
                print("\r\t\u2192 Try Proxy again ...")
                proxies = proxy.local()
                print("\r"+" "*60, end="")
                if proxies is None:
                    print("\r"+" "*60, end="")
                    flag = input(
                       "\r\t\u2192 Failed twice. Continue without proxy [Y/n] "
                       )
                    proxies = None
                    if flag == "n":
                        exit(1)
        return proxies
