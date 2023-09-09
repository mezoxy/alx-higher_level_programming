#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    b = ()
    if len(tuple_a) > 1:
        if len(tuple_b) > 1:
            b = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
            return b
        elif len(tuple_b) == 1:
            b = tuple_a[0] + tuple_b[0], tuple_a[1]
            return b
        b = tuple_a[0], tuple_a[1]
        return b
    else:
        if len(tuple_b) > 1:
            return add_tuple(tuple_b, tuple_a)
        else:
            return add_tuple(tuple_b, tuple_a)
