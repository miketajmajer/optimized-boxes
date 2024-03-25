import os
import unittest
from boxes.box import Box
from boxes.input import read_data
from boxes.output import print_results
from boxes.solution import find_solution, SolutionType


# Load data and fix solution
class TestExample1(unittest.TestCase):
    def test_example0(self):
        containers = []
        boxes = []
        stored_boxes = []
        extra_boxes = []
        free_space = []

        # Test Example0 - all boxes should fit in both cases
        read_data(os.path.join(os.path.dirname(__file__), 'example0.dat'), containers, boxes)
        container = containers[0]
        find_solution(SolutionType.MOST_VOLUME, containers, boxes, stored_boxes, extra_boxes, free_space)
        self.assertEqual(containers, [])
        self.assertEqual(extra_boxes, [])
        self.assertEqual(free_space, [])

        find_solution(SolutionType.MOST_BOXES, containers, boxes, stored_boxes, extra_boxes, free_space)
        self.assertEqual(containers, [])
        self.assertEqual(extra_boxes, [])
        self.assertEqual(free_space, [])

    def test_example1(self):
        containers = []
        boxes = []
        stored_boxes = []
        extra_boxes = []
        free_space = []

        # Test Example1
        read_data(os.path.join(os.path.dirname(__file__), 'example1.dat'), containers, boxes)
        container = containers[0]
        find_solution(SolutionType.MOST_VOLUME, containers, boxes, stored_boxes, extra_boxes, free_space)
        print_results('example1 - volume', container, stored_boxes, extra_boxes, free_space)
        find_solution(SolutionType.MOST_BOXES, containers, boxes, stored_boxes, extra_boxes, free_space)
        print_results('example1 - most boxes', container, stored_boxes, extra_boxes, free_space)





