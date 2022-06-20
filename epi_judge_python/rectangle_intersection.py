import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName

Rect = collections.namedtuple("Rect", ("x", "y", "width", "height"))


def intersect_rectangle(r1: Rect, r2: Rect) -> Rect:
    if r2.x < r1.x:
        temp = r1
        r1 = r2
        r2 = temp

    if r2.x > r1.x + r1.width:
        return Rect(0, 0, -1, -1)
    else:
        if r1.y + r1.height < r2.y or r1.y > r2.y + r2.height:
            return Rect(0, 0, -1, -1)

    if r1.x + r1.width < r2.x + r2.width:
        wid = r1.x + r1.width - r2.x
    else:
        wid = r2.width

    if r1.y <= r2.y:
        yv = r2.y
        if r2.y + r2.height <= r1.y + r1.height:
            ht = r2.height
        else:
            ht = r1.y + r1.height - r2.y
    else:
        yv = r1.y
        if r1.y + r1.height <= r2.y + r2.height:
            ht = r1.height
        else:
            ht = r2.y + r2.height - r1.y
    print(Rect(r2.x, yv, wid, ht))
    return Rect(r2.x, yv, wid, ht)


def intersect_rectangle_wrapper(r1, r2):
    return intersect_rectangle(Rect(*r1), Rect(*r2))


def res_printer(prop, value):
    def fmt(x):
        return [x[0], x[1], x[2], x[3]] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "rectangle_intersection.py",
            "rectangle_intersection.tsv",
            intersect_rectangle_wrapper,
            res_printer=res_printer,
        )
    )
