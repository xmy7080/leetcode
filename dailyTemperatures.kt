//use of monotonic stack
data class TempIdx(
    val temp: Int,
    val idx: Int
)
class Solution {
    fun dailyTemperatures(temperatures: IntArray): IntArray {
        // use of data class
        val stack = ArrayDeque<TempIdx>()
        val result = IntArray(temperatures.size){0}
        for(i in temperatures.size -1 downTo 0){
            while(stack.size > 0 && stack.first()!!.temp <= temperatures[i]){
                stack.removeFirst()
            }
            if(stack.isNotEmpty()) result[i] = stack.first()!!.idx - i
            stack.addFirst(TempIdx(temperatures[i], i) )
        }
        return result

        // val stack = ArrayDeque<IntArray>()
        // val res = IntArray(temperatures.size){0}
        // for(i in temperatures.length-1 downTo 0){
        //     while(stack.size > 0 && stack.first()!![0] < temperatures[i]) {
        //         stack.removeFirst()
        //     }
        //     if(stack.first() != null){
        //         res[i] = stack.first()!![1] - i
        //     }
        //     stack.addFirst(intArrayOf(temperature[i], i))
        // }
        // return res
    }
}
