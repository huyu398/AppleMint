# -*- coding: utf-8 -*-

import numpy as np

def get_prime_numbers(max_num):
    sequence = np.array(range(2, max_num + 1))
    prime_numbers = []
    while sequence.any():
        # 素数を取り出す
        p_num = sequence[0]
        # 現在の素数以前で割っているので，最大値が素数の二乗より小さいなら配列には素数しか残っていない
        if p_num ** 2 > max_num:
            break
        # 素数を追加する
        prime_numbers.append(p_num)
        # 素数で全体を割っていく
        sequence = sequence[sequence % p_num != 0]
    prime_numbers += list(sequence)
    return prime_numbers

print('10 以下の素数の和は', sum(get_prime_numbers(10)))
# sum() では overflow する
print('200 万以下の素数の和は', np.sum(get_prime_numbers(2000000), dtype=np.uint64))
