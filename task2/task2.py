import sys
import argparse


def add_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('file_1', type=argparse.FileType())
    parser.add_argument('file_2', type=argparse.FileType())
    return parser


if __name__ == '__main__':
    parse = add_arguments()
    args = parse.parse_args(sys.argv[1:])
    f1 = args.file_1.readlines()
    f2 = args.file_2.readlines()
    circles = []
    for line in f1:
        if line:
            circles.append([float(x) for x in line.split()])
    dots = []
    for line in f2:
        if line:
            dots.append([float(x) for x in line.split()])


    def where_is_the_dot(x0, y0, r, x1, y1):
        x1 -= x0
        y1 -= y0
        delta = x1 ** 2 + y1 ** 2
        r **= 2
        if delta == r:
            print('0 - точка лежит на окружности\n')
        elif delta < r:
            print('1 - точка внутри\n')
        else:
            print('2 - точка снаружи\n')

    for circle in circles:
        x0 = circle[0]
        y0 = circle[1]
        r = circle[2]
        for dot in dots:
            x1 = dot[0]
            y1 = dot[1]
            where_is_the_dot(x0, y0, r, x1, y1)
