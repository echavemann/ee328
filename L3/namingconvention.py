
import math
def combination_calculator(n, k): #function that takes in two numbers (n and k)
    if k > n: #if k is greater than n, return 0
         return 0 #return 0
    else: #otherwise
         return math.factorial(n) / (math.factorial(k) * math.factorial(n-k)) #return the combination

def derivativeCalculator(f, x, h): #function that takes in a function (f), a number (x), and a number (h)
    return (f(x+h) - f(x)) / h #return the derivative of the function

def dictbreaker(input): #function that takes in a list
    list1 = [i for i in input.values()]
    b = [x for x in input]

    return (list1, b)
    


        