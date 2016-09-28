def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num-1)


if __name__ == '__main__':
    import random
    num = random.randint(0, 10)
    print "factorial of {0}".format(num)
    print factorial(num)
