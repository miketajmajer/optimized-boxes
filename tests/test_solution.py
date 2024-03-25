import unittest
from boxes.box import Box, FitType


# Test Solution Results
class TestSolution(unittest.TestCase):
    def test_split_width(self):
        container = Box('', 10, 10, 10)
        long_box = Box('', 10, 5, 5)

        # should split into 2 blocks: back 1/2 and top 1/2
        split_block = container.subtract_volume(long_box)

        self.assertEqual(split_block[0].width, 10)
        self.assertEqual(split_block[0].length, 5)
        self.assertEqual(split_block[0].height, 10)

        self.assertEqual(split_block[1].width, 10)
        self.assertEqual(split_block[1].length, 5)
        self.assertEqual(split_block[1].height, 5)

    def test_split_length(self):
        container = Box('', 10, 10, 10)
        wide_box = Box('', 5, 10, 5)

        # should split into 2 blocks: back 1/2 and top 1/2
        split_block = container.subtract_volume(wide_box)

        self.assertEqual(split_block[0].width, 5)
        self.assertEqual(split_block[0].length, 10)
        self.assertEqual(split_block[0].height, 10)

        self.assertEqual(split_block[1].width, 5)
        self.assertEqual(split_block[1].length, 10)
        self.assertEqual(split_block[1].height, 5)

    def test_split_height(self):
        container = Box('', 10, 10, 10)
        tall_box = Box('', 5, 5, 10)

        # should split into 2 blocks: back 1/2 and top 1/2
        split_block = container.subtract_volume(tall_box)

        self.assertEqual(split_block[0].width, 5)
        self.assertEqual(split_block[0].length, 10)
        self.assertEqual(split_block[0].height, 10)

        self.assertEqual(split_block[1].width, 5)
        self.assertEqual(split_block[1].length, 5)
        self.assertEqual(split_block[1].height, 10)

    def test_split_all(self):
        container = Box('', 10, 10, 10)
        small_box = Box('', 5, 5, 5)

        # should split into 2 blocks: back 1/2 and top 1/2
        split_block = container.subtract_volume(small_box)

        self.assertEqual(split_block[0].width, 5)
        self.assertEqual(split_block[0].length, 10)
        self.assertEqual(split_block[0].height, 10)

        self.assertEqual(split_block[1].width, 5)
        self.assertEqual(split_block[1].length, 5)
        self.assertEqual(split_block[1].height, 10)

        self.assertEqual(split_block[2].width, 5)
        self.assertEqual(split_block[2].length, 5)
        self.assertEqual(split_block[2].height, 5)
