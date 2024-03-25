from boxes.box import Box


def read_data(filename, container, boxes):
    with open(filename) as data:
        lines = data.readlines()

        i = 0
        for l in lines:
            l = l.strip()
            if l:
                if i == 0:
                    first = False
                    d = [i.strip() for i in l.split(',')]
                    b = Box("container", float(d[0]), float(d[1]), float(d[2]))
                    container.append(b)
                    i = i + 1
                else:
                    d = [i.strip() for i in l.split(',')]
                    b = Box("Box " + str(i), float(d[0]), float(d[1]), float(d[2]))
                    boxes.append(b)
                    i = i + 1
