import unittest
from boxes.box import Box, FitType


# Test Box Functions
class TestBoxes(unittest.TestCase):
    def test_box(self):
        box = Box("", 10, 11, 12)
        self.assertEqual(box.width, 10)
        self.assertEqual(box.length, 11)
        self.assertEqual(box.height, 12)
        self.assertEqual(box.volume, 1320)

    def test_box_contain(self):
        box = Box("", 10, 10, 10)
        same_box = Box("", 10, 10, 10)
        self.assertEqual(box.can_contain(same_box), FitType.NORMAL)
    def test_box_doesnt_contain(self):
        box = Box("", 10, 10, 10)
        big_box = Box("", 11, 10, 10)
        self.assertEqual(box.can_contain(big_box), FitType.NOT_FIT)
        big_box = Box("", 10, 11, 10)
        self.assertEqual(box.can_contain(big_box), FitType.NOT_FIT)
        big_box = Box("", 10, 10, 11)
        self.assertEqual(box.can_contain(big_box), FitType.NOT_FIT)

    def test_box_contain_rotated_up(self):
        box = Box("", 10, 20, 30)
        same_box = Box("", 30, 20, 10)
        self.assertEqual(box.can_contain(same_box), FitType.ROTATE_UP)

    def test_box_contain_rotated_ccw(self):
        box = Box("", 10, 20, 30)
        same_box = Box("", 20, 10, 30)
        self.assertEqual(box.can_contain(same_box), FitType.ROTATE_CCW)