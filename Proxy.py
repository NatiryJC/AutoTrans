#!/usr/bin/env python3

import requests
import re
import json


class proxy():
    def proxy_get():
        '''get proxy address'''
        proxies_val = []
        count = 0
        url = 'http://www.kuaidaili.com/free/inha/'
        pattern = re.compile(
                r'''<td data-title="IP">([0-9]*.[0-9]*.[0-9]*.[0-9]*)</td>
                \s*<td data-title="PORT">([0-9]*)</td>\n'''
                )
        for page in range(4, 20):
            html = requests.get(url+str(page)+'/').text
            results = pattern.findall(html)
            for item in results:
                proxy_pre = item[0]+':'+item[1]
                proxies_pre = {
                        "http": "http://"+proxy_pre,
                        "https": "https://"+proxy_pre
                        }
                if proxy.proxy_fetch(proxies_pre):
                    proxies_val.append(proxies_pre)
                    count += 1
            if count >= 2:
                break
        f = open(".proxy.json", "w")
        f.write(json.dumps(proxies_val))
        f.close()

    def proxy_delete():
        '''delete invalid proxy'''
        pass

    def proxy_fetch(proxies):
        '''proxy validity verification'''
        try:
            requests.get('http://httpbin.org/get', proxies=proxies, timeout=1)
            print("代理有效")
            return True
        # except requests.exceptions.ConnectionError:
        except:
            print("代理无效")
            return False

    def proxy_add():
        '''add proxy to proxy pool'''
        pass
