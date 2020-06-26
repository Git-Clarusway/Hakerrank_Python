# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
a=input().split()
a,b=a
b=int(b)
a=sorted(a)
for i in range(1,b+1):
    a1=list(combinations(a,i))
    a1=sorted(a1)
    # print(a1)
    for j in a1:
        a2=''.join(j)
        print(a2)


