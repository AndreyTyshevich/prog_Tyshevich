import robot
r = robot.rmap()
r.lm('task7')


def move(r, direction):
        if direction == 1:
            r.rt()
        elif direction == -1:
            r.lt()


def change_direction(direction):
    if direction == 1:
        return -1
    else:
        return 1


def can_move(r, direction):
    if direction == 1:
        return not r.wr()
    elif direction == -1:
        return not r.wl()

    return False


def task():
    direction = -1
    while True:
        if r.wl() and r.wu():
            break
        if not r.wu():
            r.up()
        elif direction == 1:
            if r.wr():
                direction = -1
            else:
                r.rt()
        else:
            if r.wl():
                direction = 1
            else:
                r.lt()

    direction = 1
    c = 0

    while True:
        if r.wu() and r.wd():
            c += 1
        else:
            c = 0

        if c > 1:
            break

        if not can_move(r, direction):
            if r.wd():
                break
            direction = change_direction(direction)
            r.dn()

        move(r, direction)

    if c > 1:
        if direction == 1:
            r.lt()
        else:
            r.rt()

        while r.wd() and r.wu():
            r.pt('red')
            move(r, direction)


r.start(task)