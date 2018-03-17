# -*- coding: utf-8 -*-

import numpy as np

def check_divisible_by_range_nums(num, range_last):
    # どんな整数も 1 で割り切れるので， range の start は 2 から
    flags = [num % i == 0 for i in range(2, range_last+1)]
    return all(flags)

def calc_min_multiple_by_range_nums(range_last):
    # 1 から range_last までの値をかける
    num = np.array(range(1, range_last+1), dtype=np.int64).prod()
    # 大きい値から順に割っていき，割っても 1 から range_last の数全てで割り切れるなら更新する
    for i in reversed(range(2, range_last+1)):
        if check_divisible_by_range_nums(num / i, range_last):
            num /= i
    return int(num)

print('1 から 10 の全ての整数で割り切れる最小の値は', calc_min_multiple_by_range_nums(10))
print('1 から 20 の全ての整数で割り切れる最小の値は', calc_min_multiple_by_range_nums(20))
