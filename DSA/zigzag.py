#  Input: N = 7, arr[] = [4, 3, 7, 8, 6, 2, 1]
#  Output: [3, 7, 4, 8, 2, 6, 1]
#  Explanation:  The given array is in zig-zag pattern as we can see 3 < 7 > 4 < 8 > 2 < 6 >1 

#  Input: N = 4, arr[] = [1, 4, 3, 2]
#  Output: [1, 4, 2, 3]

def zigzag(arr):
    arr.sort()
    print(arr)
    
if __name__ == "__main__":
    zigzag([1,2,3,4])