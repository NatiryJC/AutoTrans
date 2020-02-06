#!/usr/bin/env python3
'''Translate Engines'''


def localTrans(seq):
    '''local Translator Engines'''
    # MAX ALLOWED QUERY : 500 CHARS
    # NEED TO SPLIT PARAGRAPH INTO SENTENCES
    from translate import Translator
    Engine = Translator(to_lang='chinese')
    seq = seq.split('.')
    result = ''
    for item in seq:
        result += Engine.translate(item+'.')
    return result


def YoudaoTrans(seq):
    '''Youdao Translate API'''
    # MAX FREQUENCY LIMIT: 1000 PER HOUR
    import requests
    url = "http://fanyi.youdao.com/translate"
    data = {
            'doctype': 'json',
            'type': 'AUTO',
            'i': seq
            }
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"}
    r = requests.get(url, data=data, headers=headers)
    results = r.json()['translateResult'][0]
    result = ''
    for item in results:
        result += item['tgt']
    return result


def BaiduTrans(seq):
    import requests
    url = "http://fanyi.baidu.com/v2transapi"
    data = {
            'form': 'en',
            'to': 'zh',
            'transtype': 'translang',
            'query': seq
            }
    requests.get(url, params=data)
    pass


def GoogleTrans(seq):
    # TODO : Google Translate API
    '''Google Translate API'''
    pass
