#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    c = 0
    div = 0
    while c <= list_length:
        try:
            div = my_list_1[c] / my_list_2[c]
        except (IndexError):
            print("out of range")
        except (TypeError):
            print("wrong type")
        except (ZeroDivisionError):
            print("division by 0")
        finally:
            new_list.append(div)
    return new_list
