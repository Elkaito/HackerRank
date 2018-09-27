# Author: Kai Tanaka

#Returns the median of a list for a given index range 
def getMedian(numbers,start,end):
    size=end-start
    index=start+end
    # Odd length
    if size % 2 == 0:
        median = numbers[index//2]
    # Even length
    else:
        median = (numbers[index//2] + numbers[index//2+1]) / 2
    return int(median)
                

size = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
q1=getMedian(numbers, 0, size//2-1)
q2=getMedian(numbers, 0, size-1)
q3=getMedian(numbers, (size+1)//2, size-1)

print(q1)
print(q2)
print(q3)
