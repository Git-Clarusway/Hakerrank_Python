# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
a= input().split()
a,b=a
b=int(b)
a=sorted(a)
a=list(combinations_with_replacement(a,b))
for i in a:
    a1=''.join(i)
    print(a1)

