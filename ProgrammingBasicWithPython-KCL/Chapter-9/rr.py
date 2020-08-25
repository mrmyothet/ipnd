import time
def sum_of_n_loop(n):
    the_sum = 0
    for i in range(1,n+1):
        the_sum = the_sum + i
        return the_sum
def sum_of_n_eq(n):
    return n * (n+1) / 2
    start = time.time()
    for i in range(100000,100100):
        sum_of_n_loop(i)
        end = time.time()
        print("Time is %.7f second" % (end-start))
start = time.time()
for i in range(100000,100500):
    sum_of_n_eq(i)
    end = time.time()
print("Time is %.7f second" % (end-start))
