from enum import Enum
from boxes.boxes import Box, FitType

class SolutionType(Enum):
    MOST_VOLUME = 0
    MOST_BOXES = 1

# Find solution for a container and an array of boxes.
# Start by sorting the boxes from largest to smallest, then iterate through
# the array testing if the box fits into any containers or not.
#
# If it doesn't fit:
#   1. put the box in the filed array
#
# If it fits:
#   1. put the box in the solved list
#   2. remove the container from the free list
#   3. compute the remaining volumes and add them to the free list
#   4. sort the free list from smallest to largest
#
def find_solution(solution_type, containers, boxes, stored_boxes, extra_boxes, free_space):
    if solution_type == SolutionType.MOST_VOLUME:
        # sort boxes from largest to smallest
        boxes.sort(key=lambda b: b.volume, reverse=True)
    else:
        # sort smallest to largest, get most boxes this way
        boxes.sort(key=lambda b: b.volume)

    for box in boxes:
        DidFit = False;
        if not containers:
            extra_boxes.append(box)
        else:
            for idx, container in enumerate(containers):
                ret = container.can_contain(box)
                if ret == FitType.NOT_FIT:
                    continue

                # box fits
                DidFit = True
                stored_boxes.append(box)

                # remove container from array
                containers.pop(idx)

                if ret == FitType.NORMAL:
                    split_block = container.subtract_volume(box)
                elif ret == FitType.ROTATE_UP:
                    split_block = container.subtract_volume(box.rotate_up())
                elif ret == FitType.ROTATE_CCW:
                    split_block = container.subtract_volume(box.rotate_ccw())

                if split_block:
                    containers.extend(split_block)

                # resort the containers smaller to larger - optimize for volume or number of boxes
                if containers:
                    containers.sort(key=lambda b: b.volume)
                break

            if not DidFit:
                extra_boxes.append(box)

    free_space += containers
