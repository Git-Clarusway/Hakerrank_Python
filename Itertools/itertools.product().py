# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
a = input().split()
a=[int(i) for i in a ]
b = input().split()
b=[int(i) for i in b ]
a=product(a,b)
for i in a:
    print(i,end=' ')

