#!/usr/bin/python3
def safe print_list (my_list=[], y=0):
    x = 0
     try:
         while x is not y:
            print (my_list[x], end='')
             x += 1
    except IndexError:
        None
    print ()
    return x
