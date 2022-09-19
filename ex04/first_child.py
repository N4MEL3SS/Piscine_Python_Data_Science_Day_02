#!/usr/bin/env python3
from sys import argv
from random import randint


class Research:
    def __init__(self, path):
        self.path = path

    def file_check(self, input_file, has_header):
        lines = [line.rstrip("\n") for line in input_file]

        if len(lines) == 0:
            raise Exception("Empty file!")
        if has_header and len(lines[0].split(',')) != 2:
            raise Exception("Incorrect header struct!")

        if len(lines) < 1 + int(has_header):
            raise Exception("Incorrect file struct!")

        for i in range(int(has_header), len(lines)):
            if lines[i] != "0,1" and lines[i] != "1,0":
                raise Exception("Incorrect data struct!")
            lines[i] = lines[i].split(",")
            lines[i][0], lines[i][1] = int(lines[i][0]), int(lines[i][1])

        return lines[int(has_header):]

    def file_reader(self, has_header=True):

        try:
            with open(self.path, 'r') as input_file:
                return self.file_check(input_file, has_header)
        except FileNotFoundError as err:
            print(err)

    class Calculations:
        def __init__(self, data):
            self.data = data

        def counts(self):
            heads = 0
            tails = 0

            for pair in self.data:
                heads += pair[0]
                tails += pair[1]

            return heads, tails

        def fractions(self, heads, tails):
            first = heads / (heads + tails) * 100
            second = tails / (heads + tails) * 100

            return first, second

    class Analytics(Calculations):
        def predict_random(self, num):
            res = []

            for i in range(num):
                ran_num = randint(0, 1)
                res.append([ran_num, 1 - ran_num])

            return res

        def predict_last(self):
            if not self.data:
                raise Exception("Data is empty!")

            return self.data[-1]


if __name__ == '__main__':
    if len(argv) == 2:
        re_obj = Research(argv[1])
        data_file = re_obj.file_reader()
        calc_obj = re_obj.Calculations(data_file)
        anal_obj = re_obj.Analytics(data_file)
        head, tail = calc_obj.counts()

        print(data_file)
        print(head, tail)
        print(calc_obj.fractions(head, tail))
        print(anal_obj.predict_random(3))
        print(anal_obj.predict_last())
    else:
        print("Usage: ./first_constructor.py file_path")


# [[0, 1], [1, 0], [0, 1], [1, 0], [0, 1], [0, 1], [0, 1], [1, 0], [1, 0], [0, 1], [1, 0], [0, 1]]
# 5 7
# 41.66666666666667 58.333333333333336
