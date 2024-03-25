import os
import unittest
from boxes.box import Box
from boxes.input import read_data
from boxes.output import print_results
from boxes.solution import find_solution, SolutionType


# Load data and fix solution
class TestExample(unittest.TestCase):
    def test_example0_volume(self):
        containers = []
        boxes = []
        stored_boxes = []
        extra_boxes = []
        free_space = []

        # Test Example0 - all boxes should fit in volume case
        read_data(os.path.join(os.path.dirname(__file__), 'example0.dat'), containers, boxes)
        find_solution(SolutionType.MOST_VOLUME, containers, boxes, stored_boxes, extra_boxes, free_space)
        self.assertEqual(extra_boxes, [])
        self.assertEqual(free_space, [])

    def test_example0_boxes(self):
        containers = []
        boxes = []
        stored_boxes = []
        extra_boxes = []
        free_space = []

        # Test Example0 - the biggest box will not fit in this case due to use filling from smallest to largest
        read_data(os.path.join(os.path.dirname(__file__), 'example0.dat'), containers, boxes)
        find_solution(SolutionType.MOST_BOXES, containers, boxes, stored_boxes, extra_boxes, free_space)
        self.assertEqual(len(extra_boxes), 1)
        # box 9 is the biggest box
        self.assertEqual(extra_boxes[0].name, 'Box 9')
        # verify that we have free space
        self.assertGreater(len(free_space), 0)
