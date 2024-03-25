from enum import Enum


class FitType(Enum):
    NOT_FIT = 0
    NORMAL = 1
    ROTATE_UP = 2
    ROTATE_CCW = 3


class Box:
    name = ""
    width = 0
    length = 0
    height = 0
    volume = 0

    def __init__(self, name, width, length, height):
        self.name = name
        self.width = width
        self.length = length
        self.height = height
        self.volume = width * length * height

    # Rotate the box upwards CCW, making the width = height, and the height = width
    def rotate_up(self):
        return Box(self.name, self.height, self.length, self.width)

    # Rotate the box CCW, making the width = length, and the length =width
    def rotate_ccw(self):
        return Box(self.name, self.length, self.width, self.height)

    # We determine if a box fits into us by comparing its w, l, h with our own
    # in the same orientation. Then we rotate it up and repeat the test, finally
    # we rotate it ccw and test again. If the box doesn't satisfy any of these cases
    # it does not fit. We use an optimization by checking the volume - if the box passed in
    # has a large volume, it will never fit.
    def can_contain(self, box):
        # Optimise
        if self.volume < box.volume:
            return FitType.NOT_FIT

        # test default orientation
        if (self.length >= box.length and
            self.width >= box.width and
            self.height >= box.height):
            return FitType.NORMAL

        # test up orientation
        box_up = box.rotate_up()
        if (self.length >= box_up.length and
            self.width >= box_up.width and
            self.height >= box_up.height):
            return FitType.ROTATE_UP

        # test up orientation
        box_ccw = box.rotate_ccw()
        if (self.length >= box_ccw.length and
            self.width >= box_ccw.width and
            self.height >= box_ccw.height):
            return FitType.ROTATE_CCW

        return FitType.NOT_FIT

    # make container smaller, split if needed
    def subtract_volume(self, box):
        result = []
        # Optimize - return empty box if the volume is the same
        if self.volume == box.volume:
            return result

        # make self match the box size, returning the extra
        if self.width > box.width:
            w = self.width - box.width
            result.append(Box(self.name + ":sw", w, self.length, self.height))
            self.width = box.width

        if self.length > box.length:
            l = self.length - box.length
            result.append(Box(self.name + ":sl", self.width, l, self.height))
            self.length = box.length

        if self.height > box.height:
            h = self.height - box.height
            result.append(Box(self.name + ":sh", self.width, self.length, h))
            self.height = box.height

        return result
