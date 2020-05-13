#lt solution and easy to understand explaination
#https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/discuss/516933/C%2B%2BPython-1-line-Simple-permutation-with-explanation
#also be aware (a * b) % cap is equals to (a% cap * b%cap) % cap
from functools import reduce
class Solution:
    def countOrders(self, n: int) -> int:
        cap = 10** 9 + 7
        pickup_permutation = math.factorial(n) % cap
        delivery_permutation = reduce(lambda x,y: x*y, range(1, 2*n, 2)) % cap
        return pickup_permutation * delivery_permutation % cap
        
