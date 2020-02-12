#!/usr/bin/env python3


class read():
    def __init__(self):
        pass

    def handle_special_char(sentence):
        sentence = sentence.replace("\u0010", "")
        sentence = sentence.replace("\u0011", "")
        sentence = sentence.replace("\u0012", "")
        sentence = sentence.replace("\u0013", "")
        # sentence = sentence.replace(r"#", r"\#")
        # sentence = sentence.replace(r"%", r"\%")
        return sentence

    def txt(filename):
        sentence = []
        with open(filename, "r") as f:
            while True:
                line = f.readline()
                line = read.handle_special_char(line)
                if not line:
                    break
                line = line.strip('\n')
                sentence.append(line)
        return sentence
