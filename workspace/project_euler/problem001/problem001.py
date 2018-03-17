# -*- coding: utf-8 -*-

fizz_buzz = [fb for fb in range(1, 10) if fb % 3 == 0 or fb % 5 == 0]
print("10 未満の 3 もしくは 5 の倍数の合計:", sum(fizz_buzz))

fizz_buzz = [fb for fb in range(1, 1000) if fb % 3 == 0 or fb % 5 == 0]
print("1000 未満の 3 もしくは 5 の倍数の合計:", sum(fizz_buzz))
