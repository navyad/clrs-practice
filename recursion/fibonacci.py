def fib(num):
    if num <= 2:
        return 1
    return fib(num-1) + fib(num-2)


if __name__ == '__main__':
    import random
    num = random.randint(0, 10)
    print "fibonacci: {0}".format(num)
    print fib(num)
