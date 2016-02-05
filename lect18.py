'''name = input('What is your name?: ')
print('Hello',name)'''

import statistics

exList = [5,9,8,3,2,9,1,8,4,6,8]

x = statistics.mean(exList)
print(x)

x = statistics.median(exList)
print(x)

x = statistics.mode(exList)
print(x)

x = statistics.stdev(exList)
print(x)

x = statistics.variance(exList)
print(x)


