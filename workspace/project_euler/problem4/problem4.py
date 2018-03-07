# -*- coding: utf-8 -*-

def is_palindromic_number(num):
    num_str = str(num)
    for i in range(int(len(num_str)/2)):
        if num_str[i] != num_str[-i-1]:
            return False
    return True

multiplied_2digits_palindromics = [i * j for i in range(10**1, 10**2) for j in range(10**1, 10**2) if is_palindromic_number(i * j)]
print('2 桁の数の積で表される回文数のうち，最大のものは', max(multiplied_2digits_palindromics))

multiplied_3digits_palindromics = [i * j for i in range(10**2, 10**3) for j in range(10**2, 10**3) if is_palindromic_number(i * j)]
print('3 桁の数の積で表される回文数のうち，最大のものは', max(multiplied_3digits_palindromics))
