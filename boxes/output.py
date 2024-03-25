
#
# Output results
#
def print_results(name, container, stored_boxes, extra_boxes, free_space):
    print('Results for ' + name)

    print('Container initial volume is: %f' % container.volume)

    if stored_boxes:
        print('The following boxes fit in the container:')
        for box in stored_boxes:
            print('%s (%f, %f, %f)' % (box.name, box.width, box.length, box.height ))

        v = 0
        for box in stored_boxes:
            v = v + box.volume
        print('Stored box volume is: %f' % (v))
    else:
        print('No boxes fit')

    if extra_boxes:
        print('The following boxes did not fit:')
        for box in extra_boxes:
            print('%s (%f, %f, %f)' % (box.name, box.width, box.length, box.height ))

        v = 0
        for box in extra_boxes:
            v = v + box.volume
        print('Remaining (non stored) box volume is: %f' % (v))
    else:
        print('All boxes fit')

    if free_space:
        print('The remaining free space:')
        for box in free_space:
            print('%s (%f, %f, %f)' % (box.name, box.width, box.length, box.height ))

        v = 0
        for box in free_space:
            v = v + box.volume
        print('Unused free space volume is: %f' % (v))
    else:
        print('No remaining free space')

