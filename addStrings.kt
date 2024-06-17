class Solution {
    fun addStrings(num1: String, num2: String): String {
        var l1 = num1.length-1
        var l2 = num2.length -1
        var carry = 0
        var resList = mutableListOf<Int>()
        while (l1 >= 0 && l2 >= 0){
            val temp = num1[l1].digitToInt() + num2[l2].digitToInt() + carry
            val newVal = temp % 10
            carry = temp / 10
            resList.add(newVal)
            l1 --
            l2 --
        }
        while (l1 >= 0){
            val temp = num1[l1].digitToInt() + carry
            val newVal = temp % 10
            carry = temp / 10
            resList.add(newVal)
            l1 --
        }
        while (l2 >= 0){
            val temp = num2[l2].digitToInt() + carry
            val newVal = temp % 10
            carry = temp / 10
            resList.add(newVal)
            l2 --
        }
        if (carry != 0)
            resList.add(carry)
        return resList.reversed().joinToString("")
    }
}
