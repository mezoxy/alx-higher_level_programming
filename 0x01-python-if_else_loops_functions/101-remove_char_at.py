#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ""
    if 0 <= n < len(str):
        new_str = str[:n] + str[n + 1:]
    else:
        new_str = str
    return new_str
