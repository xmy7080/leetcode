class Solution {
    fun findDiagonalOrder(mat: Array<IntArray>): IntArray {
        val m = mat.size
        val n = mat[0].size

        var flip = false
        val res = mutableListOf<Int>()
        for(row in 0 until m + n){
            var x = 0
            var y = 0
            when{
                row < m -> {
                    x = row
                    y = 0
                }
                else -> {
                    x = m - 1
                    y = row - m + 1
                }
            }
            val tmp = mutableListOf<Int>()
            while(x in 0 until m && y in 0 until n){
                tmp.add(mat[x][y])
                x--
                y++
            }
            if(flip) res.addAll(tmp.reversed())
            else res.addAll(tmp)
            flip = !flip
        }
        return res.toIntArray()
    }
}
