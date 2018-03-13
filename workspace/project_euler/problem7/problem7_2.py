# -*- coding: utf-8 -*-

def get_prime_number(cnt):
    num = 2
    prime_numbers = [num]
    # cnt の数まで素数が求まるまで続ける
    while len(prime_numbers) < cnt:
        # 数字をインクリメントしていって，素数判定する
        num += 1
        for p_num in prime_numbers:
            # 素数で割り切れたら，素数ではない
            if num % p_num == 0:
                break
        else:
            # どの素数でも割り切れなかったら，素数に追加
            prime_numbers.append(num)
    return prime_numbers[-1]

print('6 番目の素数は', get_prime_number(6))
print('10001 番目の素数は', get_prime_number(10001))
