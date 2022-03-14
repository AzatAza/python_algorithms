import argparse
import json
import sys


def add_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('tests', type=argparse.FileType())
    parser.add_argument('values', type=argparse.FileType())
    return parser


if __name__ == '__main__':
    parse = add_arguments()
    args = parse.parse_args(sys.argv[1:])
    tests = args.tests.read()
    tests = json.loads(tests)
    values = args.values.read()
    values = json.loads(values)
    report = tests

    def get_report():
        for v in values['values']:
            for i in report['tests']:
                if v['id'] == i['id']:
                    i['value'] = v['value']
                if 'values' in i:
                    for j in i['values']:
                        if v['id'] == j['id']:
                            j['value'] = v['value']
                        if 'values' in j:
                            for k in j['values']:
                                if v['id'] == k['id']:
                                    k['value'] = v['value']
                                if 'values' in k:
                                    for m in k['values']:
                                        if v['id'] == m['id']:
                                            m['value'] = v['value']

    get_report()
    print(report)
