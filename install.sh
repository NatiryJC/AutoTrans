#!/bin/bash

pyinstaller -F AutoTrans.py
sudo cp dist/AutoTrans /usr/bin/AutoTrans
