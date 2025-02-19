class Solution {
    fun repeatedStringMatch(a: String, b: String): Int {
        var black = 0
        var white = 0
        // val count = HashSet() // first part
        val count = IntArray(26) // second part
        for(i in 0 until a.length){
            if(a[i] == b[i]) black ++
            //count.add(a[i]) // first part
            count[a[i].toInt() - 'a'.toInt()] ++ // second part
        }
        for(i in 0 until b.length){
            //if(b[i] in count) white ++ // first part
            if(count[b[i].toInt() - 'a'.toInt()]-- > 0) white ++ // second part
        }
        white -= black
        println("black " + black +  " white " + white)
        return 0
    }
}
