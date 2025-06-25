class Solution {
    fun findMinDifference(timePoints: List<String>): Int {
        val minutes = timePoints.map{toMinutes(it)}.sorted()
        val total = 60*24
        var result = total
        for(i in 0 until minutes.size - 1){
            result = min(result, minutes[i+1] - minutes[i])
        }
        result = min(result, total - (minutes[minutes.size-1] - minutes[0]) )
        return result
    }
    fun toMinutes(timePoint: String): Int{
        val hrAndMin = timePoint.split(":")
        val hr = hrAndMin[0].toInt()
        val min = hrAndMin[1].toInt()
        return hr * 60 + min
    }
}
