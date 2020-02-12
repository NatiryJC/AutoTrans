#!/usr/bin/env python3


class latex():

    def add_body(sentence):
        def handle_special_char(sentence):
            sentence = sentence.replace("\u0010", "")
            sentence = sentence.replace("\u0011", "")
            sentence = sentence.replace("\u0012", "")
            sentence = sentence.replace("\u0013", "")

            sentence = sentence.replace(r"#", r"\#")
            sentence = sentence.replace(r"%", r"\%")
            return sentence
        sentence = handle_special_char(sentence)
        body = "\n"+sentence+"\n"
        return body

    def all(sentence):
        body = sentence
        return start+body+end


start = r'''
\documentclass[11pt]{article}
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
