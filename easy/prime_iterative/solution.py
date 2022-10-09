def answer(number):
    for i in range(2,number):
        if is_prime(i)==True:
            print(i,end="")
        else:
            pass
number=int(input())
is_prime=lambda number: all(number%i != 0 for i in range(2,int(number**.5)+1))
answer(number)