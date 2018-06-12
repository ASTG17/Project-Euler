"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

a = [1,2]

def findSum(seq):
    sum = 0

    for i in seq:
        if i%2 == 0:
            sum += i

        while seq[-1] < 4000000:
            seq.append(seq[-1]+seq[-2])
    return sum


print findSum(a)


"""
seq = [1,2]

def fib(start):
    sum = 0

    while start[-1] < 10:
        for i in start:
            #if i%2 == 0:
            #    sum += i
            start.append(start[-1]+start[-2])
    return start


    for i in start:
        while i < 10:
            if i%2 == 0:
                sum += i
            start.append(start[-1]+start[-2])
    return sum

print fib(seq)

"""