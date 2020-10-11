def repl(gx_1_x, p1_px):
    print(gx_1_x, p1_px)
    return [[ None if i == None else p1_px[i-1] for i in arr] for arr in gx_1_x]


print(repl([[], [1, 3, None, None]], []))