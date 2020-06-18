#658
#use bisect_left to get the closest pivot first, then grow left and right by two pointers
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        insert = bisect.bisect_left(arr, x)
        if insert == 0:
            return arr[:k]
        elif insert == len(arr):
            return arr[-k:]
        pivot = insert-1 if abs(arr[insert-1] - x) <= abs(arr[insert] - x) else insert
        left = right = pivot
        k-= 1
        while right - left < k:
            if left == 0: right += 1
            elif right == len(arr) -1: left -= 1
            elif abs(arr[left-1] - x) <= abs(arr[right+1] - x):
                left -= 1
            else:
                right += 1
        return arr[left:right+1]
