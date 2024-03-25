import os
import argparse

from boxes.input import read_data
from boxes.output import print_results
from boxes.solution import find_solution, SolutionType


def main():
    print('Optimize Boxes')

    parser = argparse.ArgumentParser(description='Optimize Boxes')
    parser.add_argument(dest='data_file', metavar='data_file', help='Data file to optimize')
    args = parser.parse_args()

    if args.data_file:
        filename = os.path.join(os.getcwd(), args.data_file)
        print('Processing %s' % filename)
        containers = []
        boxes = []
        stored_boxes = []
        extra_boxes = []
        free_space = []

        read_data(filename, containers, boxes)
        container = containers[0]
        find_solution(SolutionType.MOST_VOLUME, containers, boxes, stored_boxes, extra_boxes, free_space)
        print_results(filename, container, stored_boxes, extra_boxes, free_space)


if __name__ == '__main__':
    main()
