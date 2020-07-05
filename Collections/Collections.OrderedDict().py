# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
n=int(input())
d=OrderedDict()
for i in range(n):
    it,_,q=input().rpartition(' ')
    d[it] = d.get(it,0)+int(q)
for i,k in d.items():
    print(i,k)

