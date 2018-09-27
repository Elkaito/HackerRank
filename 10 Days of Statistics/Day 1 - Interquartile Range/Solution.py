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
freq    = list(map(int, input().split()))
data = []
for i in range(size):
    data += [numbers[i]] * freq[i]
numElements = sum(freq)
data.sort()

q1=getMedian(data, 0, len(data)//2-1)
q3=getMedian(data, (len(data)+1)//2, len(data)-1)
interQ=q3-q1

print("%.1f" %interQ)