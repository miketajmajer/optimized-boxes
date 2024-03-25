import os
import unittest
from boxes.box import Box
from boxes.io import read_data
from boxes.solution import find_solution, SolutionType


def print_results(test_name, container, stored_boxes, extra_boxes, free_space):
    print("Results for " + test_name)

    print("Container initial volume is: %f" % container.volume)

    if stored_boxes:
        print("The following boxes fit in the container:")
        for box in stored_boxes:
            print("%s (%f, %f, %f)" % (box.name, box.width, box.length, box.height ))

        v = 0
        for box in stored_boxes:
            v = v + box.volume
        print("Stored box volume is: %f" % (v))
    else:
        print("No boxes fit")

    if extra_boxes:
        print("The following boxes did not fit:")
        for box in extra_boxes:
            print("%s (%f, %f, %f)" % (box.name, box.width, box.length, box.height ))

        v = 0
        for box in extra_boxes:
            v = v + box.volume
        print("Remaining (non stored) box volume is: %f" % (v))
    else:
        print("All boxes fit")

    if free_space:
        print("The remaining free space:")
        for box in free_space:
            print("%s (%f, %f, %f)" % (box.name, box.width, box.length, box.height ))

        v = 0
        for box in free_space:
            v = v + box.volume
        print("Unused free space volume is: %f" % (v))
    else:
        print("No remaining free space")


# Load data and fix solution
class TestExample1(unittest.TestCase):
    def test_example0(self):
        containers = []
        boxes = []
        stored_boxes = []
        extra_boxes = []
        free_space = []

        # Test Example1
        read_data(os.path.join(os.path.dirname(__file__), "example0.dat"), containers, boxes)
        container = containers[0]
        find_solution(SolutionType.MOST_VOLUME, containers, boxes, stored_boxes, extra_boxes, free_space)
        print_results("example0 - volume", container, stored_boxes, extra_boxes, free_space)
        find_solution(SolutionType.MOST_BOXES, containers, boxes, stored_boxes, extra_boxes, free_space)
        print_results("example0 - most boxes", container, stored_boxes, extra_boxes, free_space)

    def test_example1(self):
        containers = []
        boxes = []
        stored_boxes = []
        extra_boxes = []
        free_space = []

        # Test Example1
        read_data(os.path.join(os.path.dirname(__file__), "example1.dat"), containers, boxes)
        container = containers[0]
        find_solution(SolutionType.MOST_VOLUME, containers, boxes, stored_boxes, extra_boxes, free_space)
        print_results("example0 - volume", container, stored_boxes, extra_boxes, free_space)
        find_solution(SolutionType.MOST_BOXES, containers, boxes, stored_boxes, extra_boxes, free_space)
        print_results("example0 - most boxes", container, stored_boxes, extra_boxes, free_space)





