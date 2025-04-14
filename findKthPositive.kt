class Solution {
    fun findKthPositive(arr: IntArray, k: Int): Int {
        var number = 1
        var kei = k
        var idx = 0
        while(kei > 0 && idx < arr.size){
            if(arr[idx] != number) kei --
            else idx++
            number++
        }
        return number + kei - 1
    }
}
