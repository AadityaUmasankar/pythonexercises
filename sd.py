
a = [1,2,3]
b = [3,2,4]

list = []
c = len([i for i,j in zip(a,b) if i > j])
d = len([i for i,j in zip(a,b) if i < j])

list.append(c)
list.append(d)

print(list)




