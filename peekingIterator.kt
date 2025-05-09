// Kotlin Iterator reference:
// https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-iterator/
// I learned this solution the hard way...
class PeekingIterator(iteratorInput:Iterator<Int>):Iterator<Int> {
    val iterator = iteratorInput
    var presave: Int? = null
    fun peek(): Int {
    	if(presave == null) {
            presave = iterator.next()
            return presave!!
        } else {
            return presave!!
        }
    }
    
    override fun next(): Int {
        if(presave != null) {
            val temp = presave!!
            presave = null
            return temp
        }
        else return iterator.next()
    }
    
    override fun hasNext(): Boolean {
        return presave != null || iterator.hasNext()
    }
}

/**
 * Your PeekingIterator object will be instantiated and called as such:
 * var obj = PeekingIterator(arr)
 * var param_1 = obj.next()
 * var param_2 = obj.peek()
 * var param_3 = obj.hasNext()
 */
