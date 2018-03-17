# -*- coding: utf-8 -*-

import numpy as np

def get_pythagoras_number(abc_sum):
    pytha_num = []
    # a < b < c かつ a + b + c == 1000 なので， c は最大でも 997 (a == 1, b == 2)
    c_max = abc_sum - (1 + 2)
    for c in reversed(range(1, c_max + 1)):
        # a + b == 1000 - c なので， b は最大でも 999 - c (a == 1)
        b_max = abc_sum - (c + 1)
        for b in reversed(range(1, b_max + 1)):
            # a + b + c == 1000 となる a を求める
            a = abc_sum - (b + c)
            # b はループのたびに小さくなるので， a >= b となった時点で探索終了
            if a >= b: break

            # ピタゴラス数なら追加する
            if a ** 2 + b ** 2 == c ** 2:
                pytha_num.append((a, b, c))
    return pytha_num

abc_sum = 1000
abc_prod = np.array(get_pythagoras_number(abc_sum)[0]).prod()
print('a + b + c = {0} となるピタゴラス数の積 abc は'.format(abc_sum), abc_prod)
