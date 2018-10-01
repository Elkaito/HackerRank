# Author: Kai Tanaka

# Returns the ranked list
def get_rank(arr):
    elem_rank = {}
    sorted_arr = sorted(arr)
    ranked = []
    for i in range(n):
        rank = i+1
        elem_rank[sorted_arr[i]]=rank
    ranked = [elem_rank[arr[i]] for i in range(n)]
    return ranked

# Calculates the difference d_i
def get_diff(x,y):
    r_x = get_rank(x)
    r_y = get_rank(y)
    d = [(r_x[i] -  r_y[i])for i in range(n) ]
    return d


# Returns the Spearman's rank correlation coefficient
def get_spearman_rank(x,y):
    d = get_diff(x,y)
    d_square = [x**2 for x in d]
    return 1 - (6*sum(d_square)) / (n * ((n**2)-1))

# Get input
n = int(input())
x = list(map(float,input().strip().split()))
y = list(map(float,input().strip().split()))
# Get and print result
result = get_spearman_rank(x,y)
print("%.3f" %result)
