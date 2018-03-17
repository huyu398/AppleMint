# -*- coding: utf-8 -*-

import numpy as np

def get_prime_number(cnt):
    num = 2
    prime_numbers = [num]
    # cnt の数まで素数が求まるまで続ける
    while len(prime_numbers) < cnt:
        # 素数で割り切れない数字が出るまでインクリメント
        while (num % np.array(prime_numbers) == 0).any():
            num += 1
        # 素数で割り切れない数字は素数なので追加
        prime_numbers.append(num)
    return prime_numbers[-1]

print('6 番目の素数は', get_prime_number(6))
print('10001 番目の素数は', get_prime_number(10001))
