# -*- coding: utf-8 -*-

import numpy as np

def get_max_prod_and_sequence(num, digits):
    # num から digits 個の連続する数字を取り出したときの全パターン
    sequences_by_digits = [num[i:i+digits] for i in range(len(num)-digits+1)]
    # 連続する数字の全パターンに対して，各桁での総積を求める
    prod_by_sequence = [np.prod([int(num) for num in sequence], dtype=np.uint64) for sequence in sequences_by_digits]

    # 最大値の取り出し
    max_prod = max(prod_by_sequence)
    # 最大値を取る連続数の取り出し
    max_sequence = sequences_by_digits[np.argmax(prod_by_sequence)]
    return max_prod, max_sequence

thousand_num = \
    '73167176531330624919225119674426574742355349194934' \
    '96983520312774506326239578318016984801869478851843' \
    '85861560789112949495459501737958331952853208805511' \
    '12540698747158523863050715693290963295227443043557' \
    '66896648950445244523161731856403098711121722383113' \
    '62229893423380308135336276614282806444486645238749' \
    '30358907296290491560440772390713810515859307960866' \
    '70172427121883998797908792274921901699720888093776' \
    '65727333001053367881220235421809751254540594752243' \
    '52584907711670556013604839586446706324415722155397' \
    '53697817977846174064955149290862569321978468622482' \
    '83972241375657056057490261407972968652414535100474' \
    '82166370484403199890008895243450658541227588666881' \
    '16427171479924442928230863465674813919123162824586' \
    '17866458359124566529476545682848912883142607690042' \
    '24219022671055626321111109370544217506941658960408' \
    '07198403850962455444362981230987879927244284909188' \
    '84580156166097919133875499200524063689912560717606' \
    '05886116467109405077541002256983155200055935729725' \
    '71636269561882670428252483600823257530420752963450'

max_prod, max_sequence = get_max_prod_and_sequence(thousand_num, 4)
print('与えられた 1000 桁の数字のうち，隣接する 4 個の数字の総乗の中で最大となる値は {0} で {1}'.format(max_sequence, max_prod))
max_prod, max_sequence = get_max_prod_and_sequence(thousand_num, 13)
print('与えられた 1000 桁の数字のうち，隣接する 13 個の数字の総乗の中で最大となる値は {0} で {1}'.format(max_sequence, max_prod))
