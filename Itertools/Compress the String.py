# Sample Input
# 1222311
# Sample Output
# (1, 1) (3, 2) (1, 3) (2, 1)
# 8:50
# Explanation
# First, the character 1  occurs only once. It is replaced by
# (1,1). Then the character 2 occurs three times, and it is replaced by (3,2) and so on.
# Also, note the single space within each compression and between 
# the compressions.
t,x= input(),0
a=t+str(int(t)%10+1)
for i in range(len(a)-1):
    x+=1
    if a[i]!=a[i+1]:
        print((x,int(a[i])),end=' ')
        x=0 