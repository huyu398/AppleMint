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

def is_amicable(num):
    # 真の約数を求めて総和を求める
    sum_divisor = sum(get_divisor(num)[:-1])
    # 総和が num と等しければ友愛数でない
    if num == sum_divisor: return False
    # 総和の真の約数の総和が num と等しければ友愛数
    return num == sum(get_divisor(sum_divisor)[:-1])

# 10000 未満の友愛数を求める
amicable_nums = [i for i in range(10000) if is_amicable(i)]
print('10000 未満の友愛数の総和は', sum(amicable_nums))
