# coding: utf-8

fizz_buzz = 0
10.times do |num|
    fizz_buzz += num if num % 3 == 0  or num % 5 == 0
end
puts("10 未満の 3 もしくは 5 の倍数の合計: #{fizz_buzz}")

fizz_buzz = 0
1000.times do |num|
    fizz_buzz += num if num % 3 == 0  or num % 5 == 0
end
puts("1000 未満の 3 もしくは 5 の倍数の合計: #{fizz_buzz}")
