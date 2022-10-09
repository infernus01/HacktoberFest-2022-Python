def Sum(n):
    
    if n<10:
        return n
    else:
        return n%10 + Sum(n//10)
n=int(input())
print(Sum(n))


# n=int(input())
