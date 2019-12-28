name = input('Enter your name: ')
print('your name is ' +name)

age = input('Enter your age: ')
try:
    age = int(age)
except:
    print('age is invalid')
    quit()
if age<0:
    print('you entered a negative age dumbass!!')
    quit()
hundred_age = (2017-abs(age))+100
print('{}, your age will become 100 in the year {}'.format(name,hundred_age))
