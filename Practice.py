# friends = ['Aaditya', 'Deepika', 'Sandhya']
# for friend in friends:
   # print ('Happy Anniversary: ',friend) 
   # print(' '.join(['Happy Anniversary:',friend]))
  
  
# list = [x*x for x in range(20)]
# print (list)
# from random import randint
# list_random = [randint(0,174) for x in range(20) ]
# print(list_random)
# largest = None
# print (largest)
# for i in list_random:
   # if largest is None or i>largest:
      # largest = i
   # print('Loop:',i,largest)
# print('Largest:',largest)

# while True:
   # line = input('>>>')
   # if line[0] == '#':
      # continue
   # if line == 'done':
      # break
   # print (line)
# print ('Done')

# smallest = None
# largest = None
# while True:
    # line = input('>>>enter a number:')
    # if line == 'done': break
    # try:
        # user_input = float(line)
        # print(user_input)
    # except:
        # print('Invalid Input')
        # continue
    # if smallest is None:
       # smallest = user_input
    # if largest is None:
       # largest = user_input
    # if user_input > largest:
       # largest = user_input
    # elif user_input < smallest:
       # smallest = user_input
# print('Minimum:',smallest)
# print('Maximum:',largest)

# def count(word, letter):
    # count1 = 0    
    # for i in word:
        # if i == letter:
          # count1 += 1
    # return count1

import matplotlib.pyplot as plt


plt.plot(x,y)

plt.show()

