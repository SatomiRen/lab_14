#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    tpl = lambda a, b: (a, b)
    a = tpl(1, 2)
    print(a)
    b = tpl(3, a)
    print(b)
    c = tpl(a, b)
    print(c)
