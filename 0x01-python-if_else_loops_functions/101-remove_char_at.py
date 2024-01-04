#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        return (str)
    return (str[n+1:] + str[:n])
