class Solution {
    fun minWindow(s: String, t: String): String {
        val dic = hashMapOf<Char, Int>()
        // val subdic = hashMapOf<Char, Int>()
        for(c in t){
            val count = dic.getOrPut(c) {0}
            dic[c] = count + 1
            // subdic[c] = 0
        }
        var l = 0
        var r = 0
        var missingCount = t.length
        var res = s
        var found = false
        while(l <= r && r < s.length){
            // get next valid substring
            while(missingCount > 0 && r < s.length){
                val c = s[r]
                if(c in dic){
                    dic[c] = dic[c]!! - 1
                    if(dic[c]!! >= 0 )
                        missingCount --
                }
                r ++
            }
            // println("r is $r")
            while(missingCount == 0 && l < r){
                // println("in 2nd while, l is $l, r is $r")
                if(res.length >= r -l){
                    res = s.substring(l, r)
                    found = true
                }
                val c = s[l]
                if(c in dic){
                    dic[c] = dic[c]!! + 1
                    if(dic[c]!! > 0)
                        missingCount ++
                }
                l++
            }
        }

        return if(found) res else ""
    }
}
