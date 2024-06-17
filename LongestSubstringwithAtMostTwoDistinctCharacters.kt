class Solution {
    fun lengthOfLongestSubstringTwoDistinct(s: String): Int {
        val K = 2
        var l = 0
        var r = 0
        var maxl = 0
        var hmap = HashMap<Char, Int>()
        while (r < s.length) {
            if (hmap.size <= K && r < s.length) {
                if (s[r] !in hmap) hmap[s[r]] = 1
                else hmap[s[r]] = hmap[s[r]]!! + 1
                r ++
            }
            while (hmap.size > K) {
                hmap[s[l]] = hmap[s[l]]!! - 1
                if (hmap[s[l]] == 0) hmap.remove(s[l])
                l ++
            }
            maxl = maxOf(maxl, r - l)
        }
        return maxl
    }
}
