# -*- coding: utf-8 -*-

def fibonacci(max_val):
    x = 0
    y = 1
    while x + y <= max_val:
        yield x + y
        tmp = y
        y += x
        x = tmp

print("項が 100 以下のフィボナッチ数列: ", [i for i in fibonacci(100)])

even_fb_sum = sum([i for i in fibonacci(4000000) if not i % 2])
print("項が 400 万以下の偶数のフィボナッチ数の総和: ", even_fb_sum)
