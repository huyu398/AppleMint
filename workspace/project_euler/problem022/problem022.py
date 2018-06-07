# -*- coding: utf-8 -*-

def get_name_score(name, order):
    # 名前のスコアを返す
    return sum([ord(c) - ord('A') + 1 for c in name]) * order

with open('./names.txt', 'r') as f:
    name_list = f.read().split(',')

# name には先頭と末尾に '"' が含まれている
all_score = sum([get_name_score(name[1:-1], i+1) for i, name in enumerate(sorted(name_list))])
print('ファイル中の全名前のスコアの合計は', all_score)
