class Solution {
    fun minAddToMakeValid(s: String): Int {
        var leftUnpair = 0
        var rightUnpair = 0
        for (c in s) {
            when (c){
                '(' -> leftUnpair++
                ')' -> if(leftUnpair > 0) leftUnpair--
                        else rightUnpair++
            }
        }
        return leftUnpair + rightUnpair
    }
}
