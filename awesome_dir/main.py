import argparse
import logging
from datetime import datetime

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

    outputFile = ''

    parser = argparse.ArgumentParser(description='Solve awesome HashCode 2019')
    parser.add_argument('--input', metavar='N', type=str, required=True,
                        dest="input_file_name", help='input file')
    parser.add_argument('--output', type=str, dest="output_file_name",
                        required=True, help='output file')
    parser.add_argument('--debug', action='store_true',
                        help='add for debug logs')
    args = parser.parse_args()

    setup_logging(args.debug)

    input_file_name = args.input_file_name
    output_file_name = args.output_file_name

    problem = load_file(input_file_name + '.in')

    solution = solve(problem)

    export(output_file_name, solution)
