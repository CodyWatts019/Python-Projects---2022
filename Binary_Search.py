"""
In this program we will find a specific number or integer in an array using binary seach.
It is a searching method in which the program will add the first and last index and divide it by 2.
Then it will search for the value in one of those parts of the array. 
The benifit of using binary seatch is that it can very easily pin point the value we are searching.
"""

#We will create an arry
#Take user input from the user
#Add the first and last value of the array.Then divided it by 2.
#Make the program search the number using for or if else statements.

#Function that takes a list and target parameter
#Multiple variables; middle, start, end, steps
#Recursion or while loop

def bianary_search(list,elements):
    middle = 0
    start = 0
    end = len(list)
    steps = 0

    while(start<=end):
        print("Steps", steps, ":", str(list[start:end+1]))

        steps = steps+1
        middle = (start + end)//2

        if elements == list[middle]:
            return middle
        if elements < list[middle]:
            end = middle-1
        else:
            start = middle+1
    return-1
my_list = [1,2,3,4,5,6,7,8,9]
target = 2

bianary_search(my_list,target)

