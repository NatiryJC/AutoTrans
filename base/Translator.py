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
    '''Baidu Translate API'''
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


def GoogleTrans(content, proxies=None):
    '''Google Translate API'''
    import execjs
    from urllib.request import quote
    import requests

    class Py4Js():
        """Get encrypted variables : tk"""
        def __init__(self):
            JS_Code = r"""
            function TL(a) {
                var k = "";
                var b = 406644;
                var b1 = 3293161072;
                var jd = ".";
                var $b = "+-a^+6";
                var Zb = "+-3^+b+-f";
                for (var e = [], f = 0, g = 0; g < a.length; g++) {
                    var m = a.charCodeAt(g);
                    128 > m ? e[f++] = m : (2048 > m ? e[f++] = m >> 6 | 192 : (55296 == (m & 64512) && g + 1 < a.length && 56320 == (a.charCodeAt(g + 1) & 64512) ? (m = 65536 + ((m & 1023) << 10) + (a.charCodeAt(++g) & 1023),
                    e[f++] = m >> 18 | 240,
                    e[f++] = m >> 12 & 63 | 128) : e[f++] = m >> 12 | 224,
                    e[f++] = m >> 6 & 63 | 128),
                    e[f++] = m & 63 | 128)
                }
                a = b;
                for (f = 0; f < e.length; f++) a += e[f],
                a = RL(a, $b);
                a = RL(a, Zb);
                a ^= b1 || 0;
                0 > a && (a = (a & 2147483647) + 2147483648);
                a %= 1E6;
                return a.toString() + jd + (a ^ b)
            };
            function RL(a, b) {
                var t = "a";
                var Yb = "+";
                for (var c = 0; c < b.length - 2; c += 3) {
                    var d = b.charAt(c + 2),
                    d = d >= t ? d.charCodeAt(0) - 87 : Number(d),
                    d = b.charAt(c + 1) == Yb ? a >>> d: a << d;
                    a = b.charAt(c) == Yb ? a + d & 4294967295 : a ^ d
                }
                return a
            }
            """
            self.ctx = execjs.compile(JS_Code)

        def getTk(self, text):
            return self.ctx.call("TL", text)

    js = Py4Js()
    tk = js.getTk(content)
    content = quote(content)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    url = "https://translate.google.cn/translate_a/single?client=webapp&sl=en&tl=zh-CN&hl=EN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1&srcrom=0&ssel=0&tsel=0&kc=2&tk=%s&q=%s" % (tk, content)
    result = requests.get(url=url, headers=headers, proxies=proxies).text
    end = result.find("\",")
    if end > 4:
        result = result[4:end]
        return result
