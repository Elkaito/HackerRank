# Author: Kai Tanaka

if __name__ == '__main__':
    n = int(input())
    print(*[i for i in range(1,n+1)] , sep="")
    
    """
    print([1,2,3])
    #[1, 2, 3]

    print(*[1,2,3])
    #1 2 3

    print(1,2,3)
    #1 2 3
    """