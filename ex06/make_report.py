import logging
from analytics import Research
from config import *


if __name__ == '__main__':
    logging.basicConfig(filename=f'{LOG_NAME}.{LOG_EXE}', filemode='w', level=logging.DEBUG, format='%(asctime)s %(message)s')

    re_obj = Research(FILEPATH)
    data_file = re_obj.file_reader(HAS_HEADER)
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
    re_obj.send_in_telegramm("Report created success.")

else:
    print("Usage: ./first_constructor.py file_path")
