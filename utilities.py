import pyperclip                    # For Copy to ClipBoard
from termcolor import colored       # For Stylish Heading
from pyfiglet import figlet_format  # For Stylish Heading
import sys                          # For getting arguments in Terminal
import os                           # For getting Current Working Directory
import time                         # For End of Terminal Extra Time

class Style:
    # Stylised Font

    def style_font(self):
        f = figlet_format("[-  C O R R U P T   F I L E  -]", font="slant", width = 130)
        print(colored(f, "green"), end="\n\n\n")
        time.sleep(0.5)

class Corrupt:
    # Corrupt a File

    def __init__(self, name):
        self.name = name

    def corrupt_func(self):
        with open(self.name, "wb")as f:             # Can Work with both "ab" and "wb"
            f.seek(0)
            f.write(b'000000000000')
            f.close()

class Intro():
    # Intro README for Minimalistic Design

    def intro_minimal(self):
        cmd = "py -3 Corrupt_File_Minimal.py File.pdf"

        print("Enter the File name in the Terminal.")
        time.sleep(1)
        print("For example, We have to Corrupt a file with name, \"File.pdf\". So, the command for the same will be: ")
        print()
        time.sleep(1)
        print(cmd)
        time.sleep(1)

        c = input("Want to copy this Command to your Clipboard (Y/N): ")
        if c.upper() == "Y":
            pyperclip.copy(cmd)
            time.sleep(1)
            print("Command Copied")
        else:
            print("Ok")

    def intro_main(self):
        # Intro README for Main Design

        print("Enter Choice (INTEGER ONLY):")
        print("1. Corrupt a File (Existing or New)")
        print("2. Exit")
        c = int(input())
        print()

        return c
