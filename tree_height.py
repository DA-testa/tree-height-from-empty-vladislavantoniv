# python3

import sys
import threading
import numpy as np


def compute_height(n, parents):
    # Write this function
    max_height=0;
    for i in range (n):
        n=i
        count=0
        while n!=-1:
            n=parents[n]
            count=count+1
        if max_height < count:
            max_height=count
    # Your code here
    return max_height


def main():
    choose=input()
    choose_arr=[]
    parents=[]
    for i,next in enumerate(choose):
        choose_arr.append(next)
    if choose_arr[0]=="I":
        numcount=input()
        numcount=int(numcount)
        #print(type(numcount))
        #print(numcount)
        text=input()
        #print(text)
        parents=np.fromstring(text, dtype=int, sep=' ')
        #print(parents)
        #print(type(parents))
        #print("result=")
        print(compute_height(numcount,parents))
    elif choose_arr[0]=="F":
        fileName=input()
        if fileName[0]!='a':
            fileName="test/"+fileName
            with open(fileName,"r") as f:
                numcount=f.readlines()[0]
                numcount=int(numcount)
            with open(fileName,"r") as f:
                text=f.readlines()[1]
            parents=np.fromstring(text, dtype=int, sep=' ')
            print(compute_height(numcount,parents))
        
    # implement input form keyboard and from files
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    pass

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.

main()
# print(numpy.array([1,2,3]))