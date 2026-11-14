class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a,b = nums1, nums2

        if len(nums2) < len(nums1):
            a,b = b,a

        total = len(nums1) + len(nums2)
        half = total//2
        l = 0
        r = len(a) - 1

        while True:
            m = (l + r) // 2
            i = half - m -2

            aleft = a[m] if m >=0 else float("-infinity")
            aright = a[m+1] if (m+1)  < len(a) else float("infinity")
            Bleft =  b[i] if i >= 0 else float("-infinity")
            Bright = b[i+1] if (i+1) < len(b) else float("infinity")

            if aleft <= Bright and Bleft <= aright:
                if total % 2 == 1:
                    return min(aright, Bright)
                else:
                    return  ( min(aright , Bright) + max(aleft, Bleft)) / 2
            elif aleft > Bright:
                r = m-1
            else:
                l = m+1
        