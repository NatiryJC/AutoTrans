#!/usr/bin/env python3

from base import Load, Parser, Translator, Export, Proxy, Color
import argparse
options_parser = argparse.ArgumentParser("AutoTrans")
options_parser.add_argument(
        'filename',
        nargs="+",
        help="the file(s) need to be translated"
        )
options_parser.add_argument(
        '--use-proxy',
        required=False,
        action="store_true",
        help='use proxy'
        )
options_parser.add_argument(
        '-t', '--translator',
        required=False,
        default='google',
        help='Specify the Translator(local, youdao, baidu or google)'
        )
options = options_parser.parse_args()
is_proxy = options.use_proxy
filenames = options.filename
translator = options.translator
trans = {
        "google": Translator.GoogleTrans,
        "baidu": Translator.BaiduTrans,
        "youdao": Translator.YoudaoTrans,
        "local": Translator.localTrans,
        }
translator = trans[translator]


def translate(sentence):
    result = []
    for line in sentence:
        result.append(line+" "+translator(line))
    return result


if __name__ == '__main__':
    proxies = Proxy.proxy.run(is_proxy)
    Color.colored(":: Translating ...", 'red')
    for filename in filenames:
        Color.colored("\t\u2192 Load %s ..." % filename, 'pink')
        sentence = Load.read.txt(filename)
        Color.colored("\t=> Parsering and getting body ...", 'green')
        body = Parser.parser(sentence)
        Color.colored("\t=> Translating ...", 'green')
        translation = translate(body)
        Color.colored("\t=> Export into %s.md ..." % filename.split(".")[0], 'green')
        Export.markdown(translation, filename)
