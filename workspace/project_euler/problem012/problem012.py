# -*- coding: utf-8 -*-

import math

def get_divisor(num):
    # 約数を探すには，平方根までで良い
    divisor_max = math.ceil(math.sqrt(num))
    # 1 から順に平方根まで約数を探す
    divisor = [d for d in range(1, divisor_max+1) if not num % d]
    # 平方根までの約数と対応する約数を追加する
    divisor += [int(num/d) for d in reversed(divisor)]
    # 素数の二乗が重複するので，削除して返す
    return sorted(list(set(divisor)))

i = 1
tri_num = 0
divisor = []
while len(divisor) <= 500:
    tri_num += i
    divisor = get_divisor(tri_num)
    i += 1

print('500 個より多く約数をもつ最初の三角数は', tri_num)
import ipdb; ipdb.set_trace()
