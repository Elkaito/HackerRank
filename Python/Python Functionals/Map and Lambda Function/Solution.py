# Author: Kai Tanaka

cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    fib_seq = [0,1]
    [fib_seq.append(fib_seq[i-2] + fib_seq[i-1]) for i in range(2,n)]
    return(fib_seq[0:n])

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))