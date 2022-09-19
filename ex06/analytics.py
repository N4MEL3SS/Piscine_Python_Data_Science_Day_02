import os
import logging
import requests
import json
from random import randint


class Research:
    def __init__(self, path):
        self.path = path
        logging.info("Class Research init.")

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

        logging.debug("Returns heads and tails from file")

        return lines[int(has_header):]

    def file_reader(self, has_header=True):
        if not os.access(self.path, os.R_OK):
            raise Exception("File cannot be read! Check the access rights.")

        with open('data.csv', "r") as input_file:
            return self.file_check(input_file, has_header)

    class Calculations:
        def __init__(self, data):
            logging.info("Class Calculations init.")
            self.data = data

        def counts(self):
            heads = 0
            tails = 0

            for pair in self.data:
                heads += pair[0]
                tails += pair[1]

            logging.debug("Counts heads and tails")

            return heads, tails

        def fractions(self, heads, tails):
            first = heads / (heads + tails) * 100
            second = tails / (heads + tails) * 100

            logging.debug("Fractions heads and tails")

            return first, second

    class Analytics(Calculations):
        def predict_random(self, num):
            res = []

            for i in range(num):
                ran_num = randint(0, 1)
                res.append([ran_num, 1 - ran_num])

            logging.debug("Predict random generated")

            return res

        def predict_last(self):
            if not self.data:
                raise Exception("Data is empty!")

            logging.debug("Predict last send")

            return self.data[-1]

        def save_file(self, data, name, extension):
            with open(name + extension, 'w') as file:
                file.write(data)

            logging.debug("Report file created")
