# Author: Kai Tanaka

if __name__ == '__main__':
    n = int(input())
    # Neat list comprehension
    [print(i**2) for i in range(n)]
    """
    This is equivalent to:
    for i in range(n):
        print(i**2)
    """