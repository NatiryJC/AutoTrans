import ctypes
import sys


def colored(sentence, color_item):
    platform = sys.platform
    if "linux" in platform:
        tag = {
            'red': '\033[1;31;40m',
            'green': '\033[1;32;40m',
            'blue': '\033[1;36;40m',
            'pink': '\033[1;35;40m',
            'white': '\033[0m',
        }
        print(tag[color_item]+sentence+tag['white'])
    elif "win" in platform:
        STD_OUTPUT_HANDLE = -11
        std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

        def set_cmd_text_color(color, handle=std_out_handle):
            Bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
            return Bool

        def resetColor():
            set_cmd_text_color(tag["red"] | tag["green"] | tag["blue"])

        def setColor(sentence, color_item):
            set_cmd_text_color(tag[color_item])
            print(sentence)
            resetColor()
        tag = {
            "black": 0x00,
            "darkblue": 0x01,
            "darkgreen": 0x02,
            "darkskyblue": 0x03,
            "darkred": 0x04,
            "darkpink": 0x05,
            "darkyellow": 0x06,
            "darkwhite": 0x07,
            "darkgray": 0x08,
            "blue": 0x09,
            "green": 0x0a,
            "skyblue": 0x0b,
            "red": 0x0c,
            "pink": 0x0d,
            "yellow": 0x0e,
            "white": 0x0f,
        }
        setColor(sentence, color_item)
