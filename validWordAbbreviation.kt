class Solution {
    fun validWordAbbreviation(word: String, abbr: String): Boolean {
        var a = 0
        var w = 0
        var number = 0
        while(a < abbr.length && w < word.length){
            when{
                number == 0 && abbr[a] == '0' -> return false // when number is 0 and abbr[a] starts with 0, invalid abbreviation
                abbr[a].isDigit() -> {// when abbr[a] is numeric
                    number = 10 * number + (abbr[a++] - '0')
                }
                number != 0 ->{// when abbr[a] is non-numeric and number is not 0
                    w += number
                    number = 0
                }
                else -> {//if number is 0 and abbr[a] is non-numeric, abbr and word are both alphabet at the moment
                    if(abbr[a++] != word[w++]) return false
                }
            }
        }
        w += number
        if(w == word.length && a == abbr.length) return true else return false
    }
}
