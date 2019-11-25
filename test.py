import sys
import copy
if __name__ == '__main__':
    a = {'c':1}
    b = copy.deepcopy(a)
    b['c'] = 2
    print(a)
    print(b)