class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # O(log(min(m,n))) solution: binary search through the smaller array
        
        # to binsearch the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        half = (len(nums1)+len(nums2))//2+1 # upper half
        
        # start so nums2[mid] is not out of index
        left = 0 if len(nums2) >= len(nums1) else half-len(nums2)
        right = len(nums1)
        
        nums1.append(10**6+1)
        nums2.append(10**6+1)
        while right > left:
            mid = (left+right)//2
            #           3-
            if nums2[half-mid-1] >= nums1[mid]:
                left = mid + 1
            else:
                right = mid
        
        if right <= 2:
            f1 = nums1[:right]
        else:
            f1 = nums1[right-2:right]
        
        if half-right <= 2:
            f2 = nums2[:half-right]
        else:
            f2 = nums2[half-right-2:half-right]
        
        temp = sorted(f1+f2)
        
        if (len(nums1)+len(nums2)) % 2 == 1:
            return temp[-1]
        else:
            return (temp[-1]+temp[-2])/2
