import sys
import argparse


def add_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('n', type=int)
    parser.add_argument('m', type=int)
    return parser


if __name__ == '__main__':
    parse = add_arguments()
    args = parse.parse_args(sys.argv[1:])
    n = args.n
    m = args.m


    def seq(a, b):
        yield 1
        for i in range(b-1, a*b, b-1):
            c = i % a + 1
            if c == 1:
                return
            yield c
    arr = seq(n, m)
    for j in list(arr):
        print(f'{j}', end='')
