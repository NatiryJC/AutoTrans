#!/usr/bin/env python3
'''Translate Engines'''


def localTrans(content):
    '''local Translator Engines'''
    # MAX ALLOWED QUERY : 500 CHARS
    # NEED TO SPLIT PARAGRAPH INTO SENTENCES
    from translate import Translator
    Engine = Translator(to_lang='chinese')
    content = content.split('.')
    result = ''
    for item in content:
        result += Engine.translate(item+'.')
    return result


def YoudaoTrans(content):
    '''Youdao Translate API'''
    # MAX FREQUENCY LIMIT: 1000 PER HOUR
    import requests
    url = "http://fanyi.youdao.com/translate"
    data = {
            'doctype': 'json',
            'type': 'AUTO',
            'i': content
            }
    r = requests.get(url, data)
    results = r.json()['translateResult'][0]
    result = ''
    for item in results:
        result += item['tgt']
    return result


def BaiduTrans(content):
    import requests
    url = "http://fanyi.baidu.com/v2transapi"
    data = {
            'form': 'en',
            'to': 'zh',
            'transtype': 'translang',
            'query': content
            }
    requests.get(url, params=data)
    pass


def GoogleTrans(content):
    # TODO : Google Translate API
    '''Google Translate API'''
    import execjs
    from urllib.request import quote
    import requests

    class Py4Js():
        """Get encrypted variables : tk"""
        def __init__(self):
            f = open("./GetTK.js")
            JS_Code = f.read()
            f.close()
            self.ctx = execjs.compile(JS_Code)

        def getTk(self, text):
            return self.ctx.call("TL", text)

    js = Py4Js()
    tk = js.getTk(content)
    content = quote(content)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    url = "https://translate.google.cn/translate_a/single?client=webapp&sl=en&tl=zh-CN&hl=EN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1&srcrom=0&ssel=0&tsel=0&kc=2&tk=%s&q=%s" % (tk, content)
    result = requests.get(url=url, headers=headers).text
    end = result.find("\",")
    if end > 4:
        result = result[4:end]
        return result
