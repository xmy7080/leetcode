//optimal solution, count until sqrt of num, refer to editorial solution #3
class Solution {
    fun checkPerfectNumber(num: Int): Boolean {
        if(num <= 1) return false
        var sum = 1
        var divisor = 2
        while(divisor * divisor <= num){
            if(num % divisor == 0){
                sum += divisor
                if(divisor * divisor != num)
                    sum += num / divisor
            }
            divisor ++
        }
        return sum == num
    }
}
// origin solution, count until num/2
class Solution {
    fun checkPerfectNumber(num: Int): Boolean {
        return num == findDivisor(num).reduce{a, b -> a+b}
    }
    fun findDivisor(num: Int): List<Int>{
        if(num == 1) return listOf(0)
        val result = mutableListOf(1)
        var divisor = 2
        while(divisor <= num/2){
            if(num % divisor == 0)
                result.add(divisor)
            divisor ++
        }
        return result
    }
}
