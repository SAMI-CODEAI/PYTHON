from typing import List,Optional

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        length=m+n
        num1dup=nums1[:m]
        # print(num1dup)
        nums1=[]
        nums1=[0]*length
        # print(nums1)
        for i in range(m):
            nums1[i]=num1dup[i]
        # print(nums1)
        for i in range(n):
            nums1[i+m]=nums2[i]
        # print(nums1)
        return sorted(nums1)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        length=m+n
        num1dup=nums1[:m]
        # print(num1dup)
        # nums1=[]
        nums1=[x for x in nums1 if x!=0]
        # nums1=[0]*length
        # print(nums1)
        # for i in range(m):
        #     nums1[i]=num1dup[i]
        # # print(nums1)
        for i in range(n):
            nums1.append(nums2[i])
        # print(nums1)
        return sorted(nums1)







num1=[1,2,3,0,0,0]
num2=[2,5,6]
m=3
n=3
sol = Solution().merge(num1,m,num2,n)
print(sol)

