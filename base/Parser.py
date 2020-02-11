#!/usr/bin/env python3
import re


# For Document Structure
abstract_start = re.compile(r"^Abstract")
foreword_start = re.compile(r"^Foreword")
contents_start = re.compile(r"^Contents")
body_start = re.compile(r"^\d\s.*\D$")
references_start = re.compile(r"^References")

# For Body
title_1 = re.compile(r"^\d\s.*")
title_2 = re.compile(r"^\d\.\d\s.*")
title_3 = re.compile(r"^\d\.\d\.\d\s.*")
title_4 = re.compile(r"^\d\.\d\.\d\.\d\s.*")
title_5 = re.compile(r"^\d\.\d\.\d\.\d\.\d\s.*")
para_start = re.compile(r"^\s.*")

# For References
references_count = re.compile(r"^\s*(\d*).")


def readtxt():
    def handle_special_char(sentence):
        sentence = sentence.replace("\u0010", "")
        sentence = sentence.replace("\u0011", "")
        sentence = sentence.replace("\u0012", "")
        sentence = sentence.replace("\u0013", "")

        sentence = sentence.replace(r"#", r"\#")
        sentence = sentence.replace(r"%", r"\%")
        return sentence

    sentence = []
    with open("b.txt", "r") as f:
        while True:
            line = f.readline()
            line = handle_special_char(line)
            if not line:
                break
            line = line.strip('\n')
            sentence.append(line)
    return sentence


def parser(sentence):
    def split(sentence):
        abstract = []
        foreword = []
        contents = []
        body = []
        references = []
        is_abstract = False
        is_foreword = False
        is_contents = False
        is_body = False
        is_references = False
        for line in sentence:
            abstract_flag = abstract_start.search(line)
            foreword_flag = foreword_start.search(line)
            contents_flag = contents_start.search(line)
            body_flag = body_start.search(line)
            references_flag = references_start.search(line)
            if abstract_flag is not None:
                print(abstract_flag)
                is_abstract = True
                is_foreword = False
                is_contents = False
                is_body = False
                is_references = False
            if foreword_flag is not None:
                is_abstract = False
                is_foreword = True
                is_contents = False
                is_body = False
                is_references = False
            if contents_flag is not None:
                is_abstract = False
                is_foreword = False
                is_contents = True
                is_body = False
                is_references = False
            if body_flag is not None:
                is_abstract = False
                is_foreword = False
                is_contents = False
                is_body = True
                is_references = False
            if references_flag is not None:
                is_abstract = False
                is_foreword = False
                is_contents = False
                is_body = False
                is_references = True
            if is_abstract:
                abstract.append(line)
            if is_contents:
                contents.append(line)
            if is_foreword:
                foreword.append(line)
            if is_body:
                body.append(line)
            if is_references:
                references.append(line)
        return abstract, foreword, contents, body, references

    def handle_abstract(sentence):
        try:
            print(r"\abstract{"+sentence[0]+"}")
            for line in sentence[1:]:
                print(" "+line, end="")
        except IndexError:
            pass
            # print("Haven't Abstract")

    def handle_reference(sentence):
        count = 1
        for line in sentence:
            flag = references_count.findall(line)[0]
            try:
                flag = int(flag)
                if count == flag:
                    count += 1
                    print()
                    print(line, end="")
                else:
                    print(line, end="")
            except ValueError:
                print(line, end="")

    def handle_body(sentence):
        for line in sentence:
            title_1_flag = title_1.search(line)
            title_2_flag = title_2.search(line)
            title_3_flag = title_3.search(line)
            title_4_flag = title_4.search(line)
            title_5_flag = title_5.search(line)
            para_start_flag = para_start.search(line)
            if title_1_flag is not None:
                print("\n")
                # print('title 1:')
                line = line.split(". ")[-1]
                print(r"\section{"+line+"}")
                print()
                continue
            if title_2_flag is not None:
                print("\n")
                # print('title 2:')
                line = line.split(". ")[-1]
                print(r"\subsection{"+line+"}")
                print()
                continue
            if title_3_flag is not None:
                print("\n")
                # print('title 3:')
                line = line.split(". ")[-1]
                print(r"\subsubsection{"+line+"}")
                print()
                continue
            if title_4_flag is not None:
                print("\n")
                # print('title 4:')
                line = line.split(". ")[-1]
                print(line)
                print()
                continue
            if title_5_flag is not None:
                print("\n")
                # print('title 5:')
                line = line.split(". ")[-1]
                print(line)
                print()
                continue
            if para_start_flag is not None:
                print("\n")
                # print('para: ')
                print(line, end='')
                continue
            else:
                print(' '+line, end='')

    abstract, foreword, contents, body, references = split(sentence)
    # handle_abstract(abstract)
    handle_body(body)
    # handle_reference(references)


start = r'''\documentclass[11pt]{article}
\title{\textbf{Auto Translate}}
\author{AutoTrans}
\date{}

\addtolength{\topmargin}{-3cm}
\addtolength{\textheight}{3cm}

\usepackage{fontspec}
\usepackage{xeCJK}
\usepackage{CJKnumb}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{mathtools}
\usepackage{pdfpages}
\usepackage{xstring}
\usepackage{emptypage}
\usepackage[many]{tcolorbox}
\usepackage{setspace}
\usepackage{biblatex}
\usepackage{tikz}
\usepackage{pygmentex}
\usepackage{paralist}
\usetikzlibrary{shapes.symbols}
%\usepackage[iso, english]{isodate}
\usepackage{datetime}

\renewcommand{\today}{\number\year 年 \number\month 月 \number\day 日}

%\setsansfont{TeX Gyre Heros}
\setsansfont{TSCu_Times}
\setCJKmainfont{FandolSong-Regular.otf}
\setCJKsansfont{FandolHei-Regular.otf}
\setCJKmonofont{FandolHei-Regular.otf}
\setCJKfamilyfont{kai}{FandolKai-Regular.otf}
\setCJKfamilyfont{song}{FandolSong-Regular.otf}
\setCJKfamilyfont{fangsong}{FandolFang-Regular.otf}
\setCJKfamilyfont{hei}{FandolHei-Regular.otf}
\setCJKfamilyfont{hei2}{Noto Sans CJK SC}
\defaultfontfeatures{Ligatures=TeX}
\XeTeXlinebreaklocale "zh"
\XeTeXlinebreakskip = 0pt plus 1pt minus 0.1pt
\newcommand\kaiti{\CJKfamily{kai}}
\newcommand\songti{\CJKfamily{song}}
\newcommand\heiti{\CJKfamily{hei}}
\newcommand\thmheiti{\CJKfamily{hei2}}
\newcommand\fangsong{\CJKfamily{fangsong}}
\renewcommand{\em}{\bfseries\CJKfamily{emfont}}
\begin{document}
'''
end = r'''
\end{document}
'''
print(start)
sentence = readtxt()
parser(sentence)
print(end)
