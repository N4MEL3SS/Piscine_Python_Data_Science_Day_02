#!/usr/bin/env python3
from sys import argv
import os


class Research:
    def __init__(self, path):
        self.path = path

    def file_check(self, input_file):
        lines = [line.rstrip("\n") for line in input_file]

        if len(lines) < 2:
            raise Exception("Incorrect file struct!")
        if len(lines[0].split(',')) != 2 or lines[0] == "0,1" or lines[0] == "1,0":
            raise Exception("Incorrect header struct!")

        for line in lines[1:]:
            if line != "0,1" and line != "1,0":
                raise Exception("Incorrect data struct!")

        return "\n".join(lines)

    def file_reader(self):
        if not os.access(self.path, os.R_OK):
            raise Exception("File cannot be read! Check the access rights.")

        with open(self.path, 'r') as input_file:
            return self.file_check(input_file)


if __name__ == '__main__':
    if len(argv) == 2:
        obj = Research(argv[1])
        print(obj.file_reader())
    else:
        print("Usage: ./first_constructor.py file_path")
