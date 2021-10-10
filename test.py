def factors(n):
    count = 0
    k = 1
    while k*k < n:
        if n%k == 0:
            count += 1
            k += 1
        else:
            k += 1
            continue
    if k * k == n:
        return count * 2 + 1
        
    return count * 2


print(factors(10))