#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) > 1:
        if len(tuple_b) > 1:
            return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
        elif len(tuple_b) == 1:
            return (tuple_a[0] + tuple_b[0], tuple_a[1])
        return (tuple_a[0], tuple_a[1])
    elif len(tuple_b) > 1:
        return add_tuple(tuple_b, tuple_a)
    elif len(tuple_b) < 2 and len(tuple_b) < 2:
        if len(tuple_b) == 1:
            if len(tuple_a) == 1:
                return (tuple_a[0] + tuple_b[0], 0)
            return (tuple_b[0], 0)
        else:
            if len(tuple_a) == 1:
                return (tuple_a[0], 0)
            return ()
