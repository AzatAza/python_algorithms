import sys
import argparse


def add_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('file_1', type=argparse.FileType())
    return parser


if __name__ == '__main__':
    parse = add_arguments()
    args = parse.parse_args(sys.argv[1:])
    f1 = args.file_1.readlines()
    arr = []
    for line in f1:
        if line:
            arr.append(int(line))

    def get_median():
        median = sorted(arr)[len(arr) // 2]
        divider = sum(abs(el - median) for el in arr)
        print(divider)

    get_median()
