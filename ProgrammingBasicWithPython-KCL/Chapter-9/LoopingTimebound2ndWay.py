import time
def sum_of_n(n):
    start = time.time()
    the_sum = n * (n+1) / 2
    end = time.time()
    return the_sum,end-start
for i in range(5):
    print("Sum is %d , %.7f seconds" % sum_of_n(100000))
