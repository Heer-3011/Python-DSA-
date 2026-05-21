import array
class Solution:
    def findTwoElement(self, arr):
        rs=array.array('i',[])
        range1=len(arr)

        #duplicates
        for i in range(0,range1+1):    #n times
            for j in range(i+1,range1): #n times n(n)=n2sq
                if arr[i]==arr[j]:
                    rs.append(arr[j])

        #missingg
        for i in range(1,range1+1): #n
            if i not in arr:
                rs.append(i)
        return rs

arr1 = array.array('i',[4, 3, 6, 2, 1, 1])
s1=Solution()
print(s1.findTwoElement(arr1))

