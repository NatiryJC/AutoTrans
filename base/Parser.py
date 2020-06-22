#!/usr/bin/env python3
import re


# For black
black_line = re.compile(r"^\s*$")

# For Document Structure
abstract_start = re.compile(r"^Abstract")
foreword_start = re.compile(r"^Foreword")
contents_start = re.compile(r"^Contents")
body_start = re.compile(r"^\d\.*\s.*\D$")
references_start = re.compile(r"^References")

# For Body
title_1 = re.compile(r"^\d\.*\s.*")
title_2 = re.compile(r"^\d\.\d\.*\s.*")
title_3 = re.compile(r"^\d\.\d\.\d\.*\s.*")
title_4 = re.compile(r"^\d\.\d\.\d\.\d\.*\s.*")
title_5 = re.compile(r"^\d\.\d\.\d\.\d\.\d\.*\s.*")
para_start = re.compile(r"^\s\s.*")

# For References
references_count = re.compile(r"^\s*(\d*).")


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
            abstract_text = ""
            print(r"\abstract{"+sentence[0]+"}")
            for line in sentence[1:]:
                print(line, end=" ")
                abstract_text += line+" "
            return abstract_text
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
        body = []
        need_white = 0
        for line in sentence:
            # is_black_line = black_line.search(line)
            # if need_white and is_black_line is not None:
            if need_white:
                line = "  "+line
            need_white = 0
            title_1_flag = "".join(title_1.findall(line))
            title_2_flag = "".join(title_2.findall(line))
            title_3_flag = "".join(title_3.findall(line))
            title_4_flag = "".join(title_4.findall(line))
            title_5_flag = "".join(title_5.findall(line))
            para_start_flag = para_start.search(line)
            if title_1_flag != "":
                need_white = 1
                body.append(title_1_flag)
                continue
            if title_2_flag != "":
                need_white = 1
                body.append(title_2_flag)
                continue
            if title_3_flag != "":
                need_white = 1
                body.append(title_3_flag)
                continue
            if title_4_flag != "":
                need_white = 1
                body.append(title_4_flag)
                continue
            if title_5_flag != "":
                need_white = 1
                body.append(title_5_flag)
                continue
            if para_start_flag is not None:
                if line[-1]=="-":
                    body.append(line[:-1])
                else:
                    body.append(line+" ")
                continue
            else:
                if line != "":
                    if line[-1]=="-":
                        body[-1] += line[:-1]
                    else:
                        body[-1] += line+" "
        return body

    abstract, foreword, contents, body, references = split(sentence)
    return handle_body(body)
