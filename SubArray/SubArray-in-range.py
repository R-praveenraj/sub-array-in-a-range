#Given an array A of length N, return the subarray from B to C.
#A = [4, 3, 2, 6]
#B = 1
#C = 3
#  Output    [3, 2, 6]

def subArray(array,start,end):
    result=[]
    for i in range(start,end+1):
        result.append(array[i])
    return result
array=[4,3,2,6]
start=1
end=3
print(subArray(array,start,end))