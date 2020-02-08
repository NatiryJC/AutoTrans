#!/usr/bin/env python3

import requests
import re


class proxy():
    def proxy_get():
        '''get proxy address'''
        url = 'http://www.kuaidaili.com/free'
        pattern = re.compile(r'<td data-title="IP">([0-9]*.[0-9]*.[0-9]*.[0-9]*)</td>\n\s*<td data-title="PORT">([0-9]*)</td>\n')
        html = requests.get(url).text
        results = pattern.findall(html)
        for item in results:
            proxy_pre = item[0]+':'+item[1]
            proxies_pre = {
                    "http": "http://"+proxy_pre,
                    "https": "https://"+proxy_pre
                    }
        return proxies_pre

    def proxy_delete():
        '''delete invalid proxy'''
        pass

    def proxy_fetch(proxies):
        '''proxy validity verification'''
        try:
            requests.get('http://httpbin.org/get', proxies=proxies, timeout=2)
            return True
        except requests.exceptions.ConnectionError:
            print('代理无效')
            return False

    def proxy_add():
        '''add proxy to proxy pool'''
        pass
