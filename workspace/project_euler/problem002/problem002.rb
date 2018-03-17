# coding: utf-8

def fibonacci(max_val)
    x = 0
    y = 1
    while x + y <= max_val do
        yield x + y
        tmp = y
        y += x
        x = tmp
    end
end

fb = []
fibonacci(100) do |i|
    fb << i
end
puts("項が 100 以下のフィボナッチ数列: #{fb}")

even_fb = 0
fibonacci(4000000) do |i|
    even_fb += i if (i % 2).zero?
end
puts("項が 400 万以下の偶数のフィボナッチ数の総和: #{even_fb}")
