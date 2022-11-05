from snake_structure import segments

def heading_north(head=segments[0]):
    head.setheading(90)


def heading_south(head=segments[0]):
    head.setheading(270)


def heading_east(head=segments[0]):
    head.setheading(0)


def heading_west(head=segments[0]):
    head.setheading(180)

