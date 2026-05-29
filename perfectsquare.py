class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l=0
        r=num
        while l<=r:
            mid=(l+r)//2
            midsquare=mid*mid
            if midsquare>num:
                r=mid-1
            else:
                if midsquare==num:
                    return True
                l=mid+1
        return False