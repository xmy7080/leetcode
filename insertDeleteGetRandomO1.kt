class RandomizedSet() {
    val nums = mutableListOf<Int>()
    val map = mutableMapOf<Int, Int>()
    fun insert(`val`: Int): Boolean {
        if(`val` !in map){
            nums.add(`val`)
            map[`val`] = nums.size -1
            return true
        }
        return false
    }

    fun remove(`val`: Int): Boolean {
        if(`val` in map){ // swap the val to be removed with the last in the list
            val pos = map[`val`]!!
            val lastNum = nums[nums.size -1]
            map[lastNum] = pos
            nums[pos] = lastNum
            nums.removeAt(nums.size -1)
            map.remove(`val`)
            return true
        }
        return false
    }

    fun getRandom(): Int {
        return nums[Random.nextInt(nums.size)]
    }

}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * var obj = RandomizedSet()
 * var param_1 = obj.insert(`val`)
 * var param_2 = obj.remove(`val`)
 * var param_3 = obj.getRandom()
 */
