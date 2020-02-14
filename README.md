AutoTrans
=========

A translate tool via free translate API.

AutoTrans can be used to:
* Translate the text of document's main body  from 'txt' file. 

**NOTE:** Main body starts from the first heading and ends at the references.

## Installing From Source

**NOTE:** To run AutoTrans it is not needed to install. You can run it from the directory by calling `python AuotTrans.py [filename]`

First you need to resolve the dependencies AutoTrans needs. To list all dependencies by calling `cat requirements.txt`

You will at least need the following:
* Python3

* PyExecJS

* requests

* translate (optional, but recommended)

Now, you can build executable program.

`pyinstaller -F AutoTrans.py`

 And copy it to your PATH.

`sudo cp dist/AutoTrans /usr/bin/AutoTrans`

## Overview

AutoTrans [-h] [--use-proxy] [-t TRANSLATOR] filename [filename ...]