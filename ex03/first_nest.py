#!/usr/bin/env python3
import os
from sys import argv


class Research:
    def __init__(self, path):
        self.path = path

    def file_check(self, input_file, has_header):
        lines = [line.rstrip("\n") for line in input_file]

        if len(lines) == 0:
            raise Exception("Empty file!")
        if lines[0] == "0,1" or lines[0] == "1,0":
            has_header = False
        elif len(lines[0].split(',')) != 2:
            raise Exception("Incorrect header struct!")

        if len(lines) < 1 + int(has_header):
            raise Exception("Incorrect file struct!")

        for i in range(int(has_header), len(lines)):
            if lines[i] != "0,1" and lines[i] != "1,0":
                raise Exception("Incorrect data struct!")
            lines[i] = lines[i].split(",")
            lines[i][0], lines[i][1] = int(lines[i][0]), int(lines[i][1])

        return lines[int(has_header):]

    def file_reader(self):
        has_header = True
        if not os.access(self.path, os.R_OK):
            raise Exception("File cannot be read! Check the access rights.")

        with open('data.csv', 'r') as input_file:
            return self.file_check(input_file, has_header)

    class Calculations:
        def counts(self, data):
            heads = 0
            tails = 0

            for pair in data:
                heads += pair[0]
                tails += pair[1]

            return heads, tails

        def fractions(self, heads, tails):
            first = heads / (heads + tails) * 100
            second = tails / (heads + tails) * 100

            return first, second


if __name__ == '__main__':
    if len(argv) == 2:
        re_obj = Research(argv[1])
        data_file = re_obj.file_reader()
        calc_obj = re_obj.Calculations()
        print(data_file)
        head, tail = calc_obj.counts(data_file)
        print(head, tail)
        print(calc_obj.fractions(head, tail))
    else:
        print("Usage: ./first_constructor.py file_path")


# [[0, 1], [1, 0], [0, 1], [1, 0], [0, 1], [0, 1], [0, 1], [1, 0], [1, 0], [0, 1], [1, 0], [0, 1]]
# 5 7
# 41.66666666666667 58.333333333333336
