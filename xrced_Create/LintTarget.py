#!/usr/bin/python
# -*- coding: utf-8 -*-

def fib():
    x = 0  # 使っていない変数
    a, b = 1, 1

    while True:
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    for i, num in enumerate(fib()):
        print(num)
        if i >= 9:
            break
