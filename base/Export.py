#!/usr/bin/env python3
import re

# For Body
title_1 = re.compile(r"^\d\.*\s(.*)")
title_2 = re.compile(r"^\d\.\d\.*\s(.*)")
title_3 = re.compile(r"^\d\.\d\.\d\.*\s(.*)")
title_4 = re.compile(r"^\d\.\d\.\d\.\d\.*\s(.*)")
title_5 = re.compile(r"^\d\.\d\.\d\.\d\.\d\.*\s(.*)")
para_start = re.compile(r"^\s\s.*")


def markdown(sentence, filename=None):
    if filename is None:
        return
    with open(filename.split('.')[0]+".md", "w") as filename:
        for line in sentence:
            title_1_flag = "".join(title_1.findall(line))
            title_2_flag = "".join(title_2.findall(line))
            title_3_flag = "".join(title_3.findall(line))
            title_4_flag = "".join(title_4.findall(line))
            title_5_flag = "".join(title_5.findall(line))
            para_start_flag = para_start.search(line)
            if title_1_flag != "":
                print("\n"+r"# "+title_1_flag, file=filename)
                continue
            if title_2_flag != "":
                print("\n"+r"## "+title_2_flag, file=filename)
                continue
            if title_3_flag != "":
                print("\n"+r"### "+title_3_flag, file=filename)
                continue
            if title_4_flag != "":
                print("\n"+r"#### "+title_4_flag, file=filename)
                continue
            if title_5_flag != "":
                print("\n"+r"##### "+title_5_flag, file=filename)
                continue
            if para_start_flag is not None:
                print("\n"+line, file=filename)
                continue


def latex(sentence):
    # TODO
    pass


def html(sentence):
    # TODO
    pass
