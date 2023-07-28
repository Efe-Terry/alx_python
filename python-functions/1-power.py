#!/usr/bin/python3
def pow(a, b):
    result = 1
    #_ throwaway variable
    for _ in range(b):
        result *= a
    return result
