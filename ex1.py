from math import sqrt

def ex1():
    a = int(input())
    b = int(input())
    return a + b


def ex2():
    str = input()
    return len(str)

def ex3(arr):
    return [i for i in arr if is_prime(i)]


def is_prime(x):
    if (x < 2): return False
    else:
        for i in range(2, int(sqrt(x)) + 1):
            if (x % i == 0): return False
        return True 


def ex4(str):
    rs = {
        'Hoa' : 0,
        'Thuong' : 0,
        'Space' : 0
    }
    for i in str:
        if i.isupper():
            rs['Hoa'] += 1
        if i.islower():
            rs['Thuong'] += 1
        if i.isspace():
            rs['Space'] += 1

    return rs

print(ex1())
print(ex2())
print(ex3([1,2,3,4, 5, 6, 7, 8, 9, 11]))
print(ex4("ISLab  "))