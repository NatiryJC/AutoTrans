#!/usr/bin/env python3

import os

os.system('rm -rf temp')
f = open('Makefile', 'w')
seq = '''a.pdf:
\tlatexmk -xelatex -pvc- -shell-escape a.tex
'''
f.write(seq)
f.close()
os.system('python ../AutoTrans.py a.txt')
os.system('make')
os.system('cp temp/a.pdf .')
