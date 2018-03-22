# -*- coding: utf-8 -*-

import tqdm

def next_collatz(num):
    if num % 2:
        # 奇数の場合
        return num * 3 + 1
    else:
        # 偶数の場合
        return num / 2

def count_collatz_array(num):
    cnt = 1
    current_num = num
    while current_num != 1:
        current_num = next_collatz(current_num)
        cnt += 1
    return cnt

max_len = 0
for i in tqdm.tqdm(range(1, 1000000)):
    len_collatz = count_collatz_array(i)
    if len_collatz > max_len:
        max_len = len_collatz
        max_len_num = i

print('100万未満の数字の中で最長のコラッツ数列を生成する数字は', max_len_num)
