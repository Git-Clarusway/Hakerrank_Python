# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
a=input()
b=map(int,input().split())
b=Counter(b)
c=int(input())
To_m_ern=0
for i in range(c):
    s,pr=map(int,input().split())
    if b[s]!=0:
        b[s]-=1
        To_m_ern+=pr
print(To_m_ern)

