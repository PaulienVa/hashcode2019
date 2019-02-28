import argparse
import logging
from datetime import datetime
from solvers import basic

logger = logging.getLogger('main.py')


def solve(problem):
    return problem


def export(name, data):
    timestamp = datetime.now().strftime("%Y%m%d-%H%M")
    filename = timestamp + '_' + name + '.txt'

    with open('output/' + filename, 'w') as output_file:
        logger.info('Writing result to: %s', output_file.name)

        for line in data:
            output_file.write(line)


def load_file(filename):
    result = {}
    filename = filename + '.in'

    with open('input/' + filename) as input_file:
        logger.info('Writing result to: %s', input_file.name)
        lines = input_file.read().splitlines()

        [R, C, F, N, B, T] = lines[0].split(' ')

        result["rows"] = R
        result["columns"] = C
        result["vehicles"] = F
        result["ride_amount"] = int(N)
        result["bonus"] = B
        result["steps"] = T

    return result


def setup_logging(debug):
    if debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)
    logging.basicConfig(handlers=[logging.StreamHandler()])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Solve awesome HashCode 2019')
    parser.add_argument('input', type=str, nargs='+', help='input file')
    parser.add_argument('--output', type=str, dest="output",
                        help='to tag the output file')
    parser.add_argument('--debug', action='store_true',
                        help='add for debug logs')
    args = parser.parse_args()

    setup_logging(args.debug)

    for input_file in args.input:
        if args.output:
            output_file = '{}_{}'.format(args.output, input_file)
        else:
            output_file = input_file

        problem = load_file(input_file)
        solution = basic.solve(problem)
        export(output_file, solution)
