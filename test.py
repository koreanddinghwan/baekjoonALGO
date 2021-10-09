def numoffact(n):
    count,k = 0,1
    while k*k < n:
        if n%k ==0:
            count +=1
            k += 1
            
    return count


print(numoffact(7))