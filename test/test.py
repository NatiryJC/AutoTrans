#!/usr/bin/env python3

import os
import sys

opt = sys.argv[1]

if opt == '-t' or opt == '--translate':
    os.system('python ../AutoTrans.py a.txt')
    os.system('make')
    os.system('cp temp/a.pdf .')
    os.system('rm -rf temp')
elif opt == '-p' or opt == '--proxy':
    sys.path.append("./..")
    sys.path.append(".")
    from Proxy import proxy
    proxy.proxy_get()
