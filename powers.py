def powers(base,exp):
    if exp == 0:
        return 1
    if exp < 0:
        return 1.0 / base * powers(base,exp+1)  
    return base * powers(base,exp-1)
