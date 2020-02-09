#!/usr/bin/env python3

import Translator
from LaTeX import latex
from sys import argv
# TODO :
#     argv    -t --translator     specify the translator
#             -f --files          save to file(s)
#             --without_color     without color
#             -o --output         specify output file
filenames = argv[1:]


def colored(seq, color_item):
    '''print with color'''
    tag = {
            'red': '\033[1;31;40m',
            'green': '\033[1;32;40m',
            'blue': '\033[1;36;40m',
            'fuchsia': '\033[1;35;40m',
            'end': '\033[0m',
          }
    return tag[color_item]+seq+tag['end']


def count_Num(count, Num):
    '''print : show progress'''
    return '('+str(count)+'/'+str(Num)+') '


if __name__ == '__main__':
    print(colored(":: Start Translate", 'red'))
    for filename in filenames:
        print(colored("->"+filename+'\n', 'fuchsia'))
        f = open(filename, "r")
        strings = f.read()
        f.close()
        strings = strings.split(".\n")
        Num = len(strings)-1
        count = 0
        trans4latex = ''
        for seq in strings:
            if seq == '':
                continue
            else:
                seq = seq.replace('\n', ' ')+'.'
            count += 1
            trans4latex += latex.add_body(seq)
            print(colored(count_Num(count, Num)+seq, 'green'))
            translation = Translator.GoogleTrans(seq)
            trans4latex += latex.add_body(translation)
            print(colored(count_Num(count, Num)+translation, 'blue'))
        f = open(filename.split(".")[0]+".tex", "w")
        f.write(latex.all(trans4latex))
        f.close()
    print(colored(":: Translate Finish", 'red'))
    # print(latex.all(trans4latex))
