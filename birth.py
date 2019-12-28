s = [1,2,1,3,2]
d = 3
m=2

num=0
for i in range(len(s)):
    if sum(s[i:i+m])==d:
        num +=1
print(num)

# for i in range(len(s)):
# 	print(sum(s[i:i+m]))

# print(sum(s[4:10]))