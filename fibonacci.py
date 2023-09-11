#imports both random and time
import random
import time

#measures start time of function process
starttime = time.time()

#declares random variable from 15 to 35
n = random.randint(15,35)

#defines fibbunaci sequence function
def fib(n):
    counter = 0
    first = 0
    second = 1
    temp = 0

    while counter <= n:
        temp = first + second
        first = second
        second = temp
        counter = counter + 1
        if counter == n-1:
            print("fib(",first,")")

#declares function
print(fib(n))


#measures end time of function process
endtime = time.time()

#calculates function time 
tme = endtime-starttime

#prints result of time in seconds
print("fib(",str(n),") took: ",tme," seconds")


