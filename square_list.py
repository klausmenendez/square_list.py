# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def square_list(num):
    '''
    Takes a list and returns the square of each individual element. 
    '''
    for i in range(0,len(num)):
        num[i]=(num[i])**2
    print(num)
#square_list([3,5,7])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
