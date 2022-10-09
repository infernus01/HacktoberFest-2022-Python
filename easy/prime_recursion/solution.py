def Prime_Number(n,i=2):
    if n==i:
        return True
    elif n%i==0:
        return False
    return Prime_Number(n,i+1)

n=int(input())
if Prime_Number(n):
    print("0")
else:
    print("1")