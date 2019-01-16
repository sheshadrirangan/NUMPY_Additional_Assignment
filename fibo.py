# Python module script that contains fib2() method to calculate the fibonacci series till 1000

def fib2(size):
    a = 0
    b = 1
    output = []
    for i in range(size):
        if (a >= size):
            return output
        output.append(a)
        a,b = b,a+b
        
    return output

def fib1(size):
    a = 0
    b = 1
    output = []
    for i in range(size):
        output.append(a)
        a,b = b,a+b
        
    return output