#!/usr/bin/env python3


class Must_read:
    try:
        with open('data.csv', "r") as input_file:
            print(input_file.read())
    except FileNotFoundError as err:
        print(err)


if __name__ == '__main__':
    Must_read()
