import sys
import random
from time import sleep

# Heavily inspired by lawsie's IDLECOLOURS, but has been updated from 2018 to 2021 and just added a typing effect
# ---------------------------
# Typing Effect
# ---------------------------


def printt(text):
    try:
        for char in text:
            sleep(0.1)
            print(char, end='', flush=True)
    except:
        raise TypeError('Printt does not support coloured text at the moment, or you are trying to print type != str')

# This will only work in IDLE, it won't work from a command prompt
try:
    shell_connect = sys.stdout.shell
except AttributeError:
    print("idlecolors highlighting only works with IDLE, why don't you try another package such as colorama?")
    exit()

global colormap
colormap = {"red": "COMMENT",
            "orange": "KEYWORD",
            "green": "STRING",
            "blue": "stdout",
            "purple": "BUILTIN",
            "black": "SYNC",
            "brown": "console"}



# Like the print() function but will allow you to print colours
def printc(text, end="\n"):
    # Parse the text provided to find {text:color} and replace with the colour. Any text not encompassed in braces
    # will be printed as black by default.
    buff = ""
    for char in text:
        if char == "{":
            # Write current buffer in black and clear
            shell_connect.write(buff, colormap["black"])
            buff = ""
        elif char == "}":
            # Write current buffer in color specified and clear
            tag_write = buff.split(":")
            shell_connect.write(tag_write[0], tag_write[1])
            buff = ""
        else:
            # Add this char to the buffer
            buff += char

    # Write the chosen end character (defaults to newline like print)
    sys.stdout.write( end )


# Individual colour functions
def red(text):
    return "{"+ text + ":" + colormap["red"] + "}"

def orange(text):
    return "{"+ text  + ":" + colormap["orange"] + "}"

def green(text):
    return "{"+ text + ":" + colormap["green"] + "}"

def blue(text):
    return "{"+ text  + ":" + colormap["blue"] + "}"

def purple(text):
    return "{"+ text + ":" + colormap["purple"] + "}"

def black(text):
    return "{"+ text  + ":" + colormap["black"] + "}"

def brown(text):
    return "{"+ text + ":" + colormap["brown"] + "}"

def randcol(text):
    color = random.choice(list(colormap.keys()))
    return "{"+ text + ":" + colormap[color] + "}"
