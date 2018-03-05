# -*- coding: utf-8

import numpy as np

def get_prime_numbers(max_num):
    sequence = np.array(range(2, max_num + 1))
    prime_numbers = []
    while sequence.any():
        # 素数を取り出して追加
        p_num = sequence[0]
        prime_numbers.append(p_num)
        # 素数で全体を割っていく
        sequence = sequence[sequence % p_num != 0]
    return prime_numbers

def prime_factorizate(num):
    # sqrt(num) * 2 までの素数を調べれば良い
    max_root = int(np.ceil(np.sqrt(num)))
    p_nums = get_prime_numbers(max_root)
    prime_factories = [p for p in p_nums if num % p == 0]
    return prime_factories

print('13195 の素因数分解は', prime_factorizate(13195))
print('600851475143 の素因数のうち最大のものは', max(prime_factorizate(600851475143)))
