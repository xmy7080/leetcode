class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        map = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
            }
        res = [""]
        for d in digits:
            tmp = []
            for c in map[d]:
                for s in res:
                    tmp.append(s+c)
            res = tmp
        return res if digits else []
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # map = {
        #     '2':'abc',
        #     '3':'def',
        #     '4':'ghi',
        #     '5':'jkl',
        #     '6':'mno',
        #     '7':'pqrs',
        #     '8':'tuv',
        #     '9':'wxyz',
        #     }
        # res = [""]
        # for d in digits:
        #     tmp = []
        #     for t in res:
        #         for c in map.get(d):
        #             tmp.append(t+c)
        #     res = tmp
        # return res if digits else []
        
        
        
        
        
        
        
        
        
        
        
        # res = ['']
        # for d in digits:
        #     tmp = []
        #     for s in res:
        #         for c in map[d]:
        #                 tmp.append(s+c)
        #     res = tmp
        # return res if digits else []
            