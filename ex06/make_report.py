import logging
import requests
import json
from analytics import Research
from config import *


def send_in_telegramm(text):
    token = BOT_TOKEN
    chat_id = BOT_CHAT
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + \
              "&text=" + text
    results = requests.get(url_req)
    if results.status_code != 200:
        raise Exception(f'Error server {results.status_code}')


if __name__ == '__main__':
    logging.basicConfig(filename=f'{LOG_NAME}.{LOG_EXE}', filemode='w', level=logging.DEBUG, format='%(asctime)s %(message)s')

    re_obj = Research(FILEPATH)
    data_file = re_obj.file_reader()
    calc_obj = re_obj.Calculations(data_file)
    anal_obj = re_obj.Analytics(data_file)
    head, tail = calc_obj.counts()
    heads_prob, tails_prob = calc_obj.fractions(head, tail)

    calc_obj.data = anal_obj.predict_random(NUM_OF_STEPS)
    heads_predict, tails_predict = calc_obj.counts()

    text = REPORT_TEMPLATE.format(
        head + tail,
        head, tail,
        heads_prob, tails_prob,
        NUM_OF_STEPS,
        heads_predict, tails_predict
    )

    anal_obj.save_file(text, REPORT_NAME, REPORT_EXE)
    send_in_telegramm(text)

else:
    print("Usage: ./first_constructor.py file_path")
