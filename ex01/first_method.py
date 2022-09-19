#!/usr/bin/env python3


class Research:
    def file_reader(self):
        with open('data.csv', 'r') as input_file:
            return input_file.read()


if __name__ == '__main__':
    obj = Research()
    try:
        print(obj.file_reader())
    except FileNotFoundError as err:
        print(err)
