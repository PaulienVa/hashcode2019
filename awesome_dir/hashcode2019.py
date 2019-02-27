import argparse
from datetime import datetime


def solve(problem):
    return problem


def export(name, data):
    timestamp = datetime.now().strftime("%Y%m%d-%H%M")
    output_dir = './output/'
    filename = timestamp + '_' + name + '.txt'

    with open(output_dir + filename, 'w') as file:

        for line in data:
            file.write(line)


def load_file(filename):
    result = {}

    with open('input/'+ filename) as f:
        lines = f.read().splitlines()

        [R, C, F, N, B, T] = lines[0].split(' ')

        result["rows"] = R
        result["columns"] = C
        result["vehicles"] = F
        result["ride_amount"] = int(N)
        result["bonus"] = B
        result["steps"] = T

    return result


if __name__ == "__main__":

    outputFile = ''

    parser = argparse.ArgumentParser(description='Solve awesome HashCode 2019')
    parser.add_argument('--input', metavar='N', type=str, dest="inputFile",
                        help='input file(s)')
    parser.add_argument('--output', type=str, dest="outputFile",
                        help='output file(s)')

    args = parser.parse_args()
    inputFileName = args.inputFile
    outputFileName = args.outputFile
    print('Reading inputFile: ' + inputFileName)


    problem = load_file(inputFileName + '.in')

    solution = solve(problem)

    export(outputFileName, solution)

    print('Writing result to outputFile: ' + outputFileName)