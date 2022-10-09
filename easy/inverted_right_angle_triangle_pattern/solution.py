import io
from re import I


rows=int(input())
i=rows
while(i>0):
    j=i
    while(j>0):
        print('*',end='')
        j=j-1
    i=i-1
    print()