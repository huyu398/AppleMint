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
    # num == sqrt(num) ** 2 なので sqrt(num) までの素数を調べれば良い
    max_root = int(np.ceil(np.sqrt(num)))
    p_nums = get_prime_numbers(max_root)
    prime_factories = set()
    # 素数で順番に割っていく
    for p in p_nums:
        while num % p == 0:
            # 割り切れる素数を追加
            prime_factories.add(p)
            num /= p
    # 14 == 2 * 7 のような sqrt(num) 以上の素数を含む場合があるので， 1 でないなら追加
    if num != 1: prime_factories.add(int(num))
    prime_factories = list(prime_factories)
    prime_factories.sort()
    return prime_factories

print('13195 の素因数分解は', prime_factorizate(13195))
print('600851475143 の素因数のうち最大のものは', max(prime_factorizate(600851475143)))
