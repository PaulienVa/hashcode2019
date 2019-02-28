import argparse
import logging
import importlib
from datetime import datetime

logger = logging.getLogger('main.py')


def solve(problem):
    return problem


def export(name, data):
    timestamp = datetime.now().strftime("%Y%m%d-%H%M")
    filename = timestamp + '_' + name + '.txt'

    with open('output/' + filename, 'w') as output_file:
        logger.info('Writing result to: %s', output_file.name)

        output_file.write(str(len(data)) + '\n')
        for line in data:
            logger.info(line)
            output_line = " ".join(str(x) for x in line) + '\n'
            output_file.write(output_line)


def load_file(filename):
    results = []
    filename = filename + '.txt'

    with open('input/' + filename) as input_file:
        logger.info('Writing result to: %s', input_file.name)
        lines = input_file.read().splitlines()

        nr = lines[0]
        photos = lines[1:]

        for line in photos:
            els = line.split(' ')
            result = {"nr": photos.index(line),  "direction": els[0], "nTags": els[1], "tags": els[2:]}
            results.append(result)

    return nr, results


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
    parser.add_argument('--solver', required=True,
                        help='select a solver to use')
    parser.add_argument('--debug', action='store_true',
                        help='add for debug logs')
    args = parser.parse_args()

    setup_logging(args.debug)

    try:
        solver = importlib.import_module('.'.join(["solvers", args.solver]))
    except ImportError:
        logger.error("solver '%s' not available. "
                     "Create a solver in file 'solvers/%s.py'.",
                     args.solver, args.solver)
        exit(1)

    for input_file in args.input:
        if args.output:
            output_file = '{}_{}'.format(args.output, input_file)
        else:
            output_file = input_file

        nr_photos, photos = load_file(input_file)
        solution = solver.solve(photos)
        export(output_file, solution)
