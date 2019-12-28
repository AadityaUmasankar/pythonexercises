x = int(input("Enter first number:"))
y = int(input("Enter second number:"))

mx = lambda x,y : x if x > y else y

print(mx(x,y))