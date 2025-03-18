def is_top_fractal(high_prices, i):
    #检查索引是否越界
    if i < 1:
        return False
    if i >= len(high_prices)-1:
        return False
    prev_high = high_prices[i-1]
    current_high = high_prices[i]
    next_high = high_prices[i+1]

    if prev_high < current_high and next_high < current_high:
        return True
    return False

def is_bottom_fractal(low_prices, i):
    if i < 1 or i >= len(low_prices)-1:
        return False
    return low_prices[i-1] > low_prices[i] and low_prices[i] < low_prices[i+1]


high_prices=[10, 12, 15, 13, 11]
low_prices=[8, 9, 10, 9.5, 8.5,10.5]

top_fractals= [i for i in range(len(high_prices)) if is_top_fractal(high_prices, i)]
bottom_fractals=[i for i in range(len(low_prices)) if is_bottom_fractal(low_prices, i)]

print("底分型索引：",top_fractals)
print("顶分型索引：",bottom_fractals)
