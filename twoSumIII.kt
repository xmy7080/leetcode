class TwoSum() {
    val map = mutableMapOf<Int, Int>()
    fun add(number: Int) {
        map.merge(number, 1) {x, y -> x + y}
    }

    fun find(value: Int): Boolean {
        map.forEach {(num, fq) ->
            val freq = map.getOrDefault(value - num, 0)
            if ( (num * 2 == value && freq >= 2 ) || (num *2 != value && freq != 0) ) return true
        }
        return false
    }

}

/**
 * Your TwoSum object will be instantiated and called as such:
 * var obj = TwoSum()
 * obj.add(number)
 * var param_2 = obj.find(value)
 */
