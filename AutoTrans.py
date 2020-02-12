#!/usr/bin/env python3

from base import Load, Parser, Translator, Export, Proxy
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


def colored(content, color_item):
    '''print with color'''
    tag = {
            'red': '\033[1;31;40m',
            'green': '\033[1;32;40m',
            'blue': '\033[1;36;40m',
            'fuchsia': '\033[1;35;40m',
            'end': '\033[0m',
          }
    return tag[color_item]+content+tag['end']


def translate(sentence):
    result = []
    for line in sentence:
        result.append(line+" "+translator(line))
    return result


if __name__ == '__main__':
    proxies = Proxy.proxy.run(is_proxy)
    print(colored(":: Translating ...", 'red'))
    for filename in filenames:
        print(colored("\t\u2192 Load %s ..." % filename, 'fuchsia'))
        sentence = Load.read.txt(filename)
        print(colored("\t=> Parsering and getting body ...", 'green'))
        body = Parser.parser(sentence)
        print(colored("\t=> Translating ...", 'green'))
        translation = translate(body)
        print(colored("\t=> Export into %s.md ..." % filename.split(".")[0], 'green'))
        Export.markdown(translation, filename)
