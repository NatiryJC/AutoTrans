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
        default='local',
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
    def Progress(total, item, Length=60):
        precentage = int((item+1)*100/total)
        progress = "#"*int(precentage*(Length-7)/100)
        progress = "["+progress.ljust(Length-7, "-")+"]"
        precentage = " %d%%" % precentage
        print("\r\t   "+" "*Length, end="")
        print("\r\t   "+progress+precentage, end="")

    result = []
    total = len(sentence)
    Length = 60
    for item in range(0, total):
        line = sentence[item]
        result.append(line+" "+translator(line))
        Progress(total, item, Length)
    print("\r\t   "+" "*Length+"\r", end="")
    return result


if is_proxy:
    Color.colored("\r:: Try to use proxy ...", 'red')
    proxies = Proxy.proxy.run()
Color.colored("\r:: Translating ...", 'red')
for filename in filenames:
    Color.colored("\t\u2192 Load %s ..." % filename, 'pink')
    sentence = Load.read.txt(filename)
    Color.colored("\t=> Parsering and getting body ...", 'green')
    body = Parser.parser(sentence)
    Color.colored("\t=> Translating ...", 'green')
    translation = translate(body)
    filename = filename.split(".")[0]
    Color.colored("\t=> Export into %s.md ..." % filename, 'green')
    Export.markdown(translation, filename)
