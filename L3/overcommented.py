import time #import time to allow us to figure out what time it is
import multiprocessing as mp #import multiprocessing to allow us to use multiple cores
import pandas as pd #import pandas to allow us to use dataframes
import numpy as np #import numpy to allow us to use arrays

def fib(n): #function that takes in a number (n) and then generates the fibonacci sequence up to that number
    if n <= 1: #if the number is less than or equal to 1, return the number
        return n #return the value of that element in the fibonacci sequence for the recursive stack
    else: #otherwise, return the sum of the previous two elements in the fibonacci sequence
        return(fib(n-1) + fib(n-2)) #return the sum of the previous two elements in the fibonacci sequence


def pandas_function(): #function that uses pandas to multiply two dataframes
    df1 = pd.DataFrame(np.random.randn(1000, 1000)) #create a dataframe of random numbers
    df2 = pd.DataFrame(np.random.randn(1000, 1000)) #create a dataframe of random numbers
    df3 = df1 * df2 #multiply the two dataframes
    return df3 #return the dataframe

#write a function that uses newton's method to find the square root of a number
def newton_sqrt(x, n): #function that takes in a number (x) and the number of iterations (n)
    x0 = x #set the initial guess to the number
    for i in range(n): #for the number of iterations
        x1 = 0.5 * (x0 + x/x0) #use newton's method to find the square root
        x0 = x1 #set the initial guess to the new guess
    return x1 #return the square root
    



