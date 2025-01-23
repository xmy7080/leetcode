class Solution {
    fun canConstruct(ransomNote: String, magazine: String): Boolean {
        val count = hashMapOf<Char, Int>()
        magazine.forEach{
            count[it] = count.getOrDefault(it, 0) + 1
        }
        ransomNote.forEach{
            if(!count.containsKey(it) || count[it] == 0) return false
            count[it] = count[it]!! - 1
        }
        return true
    }
}
