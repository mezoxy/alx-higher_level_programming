#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    try:
        a = [0 for i in range(list_length)]
        for i in range(list_length):
            if isinstance(my_list_1[i], (int, float)):
                if isinstance( my_list_2[i], (int, float)):
                    if my_list_2[i] != 0:
                        a[i] = my_list_1[i] / my_list_2[i]
                    else:
                        a[i] = 0
                else:
                    a[i] = 0
            else:
                a[i] = 0
    except (ZeroDivisionError, IndexError, TypeError):
        if ZeroDivisionError:
            print("division by 0")
        if TypeError:
            print("wrong type")
        if IndexError:
            print("out of range")
    finally:
        return a
