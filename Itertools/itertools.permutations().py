# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
a =input().split()
a,b=a
b=int(b)
a=sorted(list(permutations(a,b)))
for i in a:
    a=''.join(i)
    print(a)

