# -*- coding: utf-8 -*-

def diff_square_sum(last_num):
    square_nums_sum = sum([i**2 for i in range(1, last_num+1)])
    nums_sum_square = sum([i for i in range(1, last_num+1)])**2
    diff = nums_sum_square - square_nums_sum
    return diff

print('最初の10個の自然数の二乗の和と和の二乗の差は', diff_square_sum(10))
print('最初の10個の自然数の二乗の和と和の二乗の差は', diff_square_sum(100))
