// chime interview question "colorMatch"
class Solution {
    fun getHint(secret: String, guess: String): String {
        var bulls = 0
        var cows = 0
        val count = IntArray(10)
        secret.forEachIndexed{idx, char ->
            if(char == guess[idx]) bulls++
            count[char.toInt() - '0'.toInt()] ++
        }
        for(char in guess){
            if(count[char.toInt() - '0'.toInt()] -- > 0) cows ++
        }
        cows = cows - bulls
        return bulls.toString() + "A" + cows.toString() + "B"
    }
}
