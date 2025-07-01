// self solution, replay the stack operations 
// and when push new process, accumulate the peak process allocated time,
// when pop old process, update the start time of the peak item after the pop
class Solution {
    data class Process(val id: Int, var start: Int)
    fun exclusiveTime(n: Int, logs: List<String>): IntArray {
        val result = IntArray(n)
        val stk = Stack<Process>()
        for(log in logs){
            val arr = log.split(":")
            val id = arr[0].toInt()
            val action = arr[1]
            when(action){
                "start" -> {
                    val start = arr[2].toInt()
                    if(stk.isNotEmpty()){
                        val prevProcess = stk.peek()
                        result[prevProcess.id] += start - prevProcess.start
                        
                    }
                    val newProcess = Process(id, start)
                    stk.push(newProcess)
                }
                "end" -> {
                    val end = arr[2].toInt()
                    val endProcess = stk.pop()
                    result[endProcess.id] += end + 1 - endProcess.start
                    if(stk.isNotEmpty()){
                        val prevProcess = stk.peek()
                        prevProcess.start = end + 1
                    }
                }
            }
        }
        return result
    }
}
