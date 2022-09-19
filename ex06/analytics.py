import os
import logging
import requests
from config import BOT_TOKEN, BOT_CHAT
from random import randint


class Research:
    def __init__(self, path):
        self.path = path
        logging.info("Class Research init.")

    def send_in_telegramm(self, text):
        token = BOT_TOKEN
        chat_id = BOT_CHAT
        url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + \
                  "&text=" + text.replace(" ", "%20")
        results = requests.get(url_req)
        if results.status_code != 200:
            logging.debug(f'Error server {results.status_code}')
            raise Exception(f'Error server {results.status_code}')
        print("Message send.")

    def file_check(self, input_file, has_header):
        lines = [line.rstrip("\n") for line in input_file]

        if len(lines) == 0:
            logging.debug("Empty file!")
            self.send_in_telegramm("Report created error!\nEmpty file!")
            raise Exception("Empty file!")
        if has_header and len(lines[0].split(',')) != 2:
            logging.debug("Incorrect header struct!")
            self.send_in_telegramm("Report created error!\nIncorrect header struct!")
            raise Exception("Incorrect header struct!")

        if len(lines) < 1 + int(has_header):
            logging.debug("Incorrect file struct!")
            self.send_in_telegramm("Report created error!\nIncorrect file struct!")
            raise Exception("Incorrect file struct!")

        for i in range(int(has_header), len(lines)):
            if lines[i] != "0,1" and lines[i] != "1,0":
                logging.debug("Incorrect data struct!")
                self.send_in_telegramm("Report created error!\nIncorrect data struct!")
                raise Exception("Incorrect data struct!")
            lines[i] = lines[i].split(",")
            lines[i][0], lines[i][1] = int(lines[i][0]), int(lines[i][1])

        return lines[int(has_header):]

    def file_reader(self, has_header=True):
        if not os.access(self.path, os.R_OK):
            logging.debug("File cannot be read!")
            self.send_in_telegramm("Report created error!\nFile cannot be read!")
            raise Exception("File cannot be read! Check the access rights.")

        with open(self.path, 'r') as input_file:
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

            logging.info("Counts heads and tails")

            return heads, tails

        def fractions(self, heads, tails):
            first = heads / (heads + tails) * 100
            second = tails / (heads + tails) * 100

            logging.info("Fractions heads and tails")

            return first, second

    class Analytics(Calculations):
        def predict_random(self, num):
            res = []

            for i in range(num):
                ran_num = randint(0, 1)
                res.append([ran_num, 1 - ran_num])

            logging.info("Predict random generated")

            return res

        def predict_last(self):
            if not self.data:
                logging.debug("Data is empty!")
                raise Exception("Data is empty!")

            logging.info("Predict last send")

            return self.data[-1]

        def save_file(self, data, name, extension):
            with open(name + extension, 'w') as file:
                file.write(data)

            logging.info("Report file created")
