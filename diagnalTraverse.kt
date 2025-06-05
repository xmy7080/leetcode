class Solution {
    fun findDiagonalOrder(mat: Array<IntArray>): IntArray {
        val m = mat.size
        val n = mat[0].size

        var flip = false
        val res = mutableListOf<Int>()
        for(row in 0 until m + n -1){ // for example , m=3, n=3, the row will only traverse from 0 to 4
            var x = 0
            var y = 0
            when{
                row < m -> { // when starts from the left most column
                    x = row // x starts from the row from 0 to m-1
                    y = 0 // y starts at first col
                }
                else -> { // when starts from the bottom row
                    x = m - 1 // x starts from bottom row
                    y = row - m + 1 // y starts from the column from 1 to n-1
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
