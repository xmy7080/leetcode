class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        dic = collections.defaultdict(int)
        for cpdomain in cpdomains:
            tmp = cpdomain.split(" ")
            count = int(tmp[0])
            domainChain = tmp[1].split('.')
            for i in xrange(len(domainChain)):
                countableDomain = '.'.join(domainChain[i:])
                dic[countableDomain] += count
        ans = []
        for key in dic:
            ans.append(str(dic[key]) + ' ' + key )
        return ans
