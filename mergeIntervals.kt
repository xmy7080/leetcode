class Solution {
    fun merge(intervals: Array<IntArray>): Array<IntArray> {
        intervals.sortBy{it[0]}
        var res = mutableListOf<IntArray>()
        var newInterval = intervals[0]
        for(itv in intervals){
            if(newInterval[1] >= itv[0]){
                newInterval[1] = maxOf(newInterval[1], itv[1])
            } else{
                res.add(newInterval)
                newInterval = itv
            }
        }
        res.add(newInterval)
        return res.toTypedArray()
    }
}
