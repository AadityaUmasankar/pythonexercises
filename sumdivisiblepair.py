ar = [1,3,2,6,1,2]
n = 6
k = 3

count = 0
for i in range(len(ar)-1):
    for x in range(1+i, len(ar)):
        # print(x)     
        if (ar[i] + ar[x]) % k == 0:
            count += 1
        
print(count)