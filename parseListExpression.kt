//lisp expression only mult and add, no let ( ADD 3 ( MULT 2 5 ) )
//should be solved by stack in O(n) time

class Solution {
    val scope = ArrayList<HashMap<String, Int>>()
    fun evaluate(expression: String): Int {
        scope.add(hashMapOf<String, Int>())
        val res = evaluateInner(expression)
        scope.removeAt(scope.size -1)
        return res
    }

    fun evaluateInner(expression: String):Int {
        if(expression[0] != '(') {
            if(expression[0].isDigit() || expression[0] == '-' )
                return expression.toInt()
            for(i in scope.size-1 downTo 0){
                if(scope[i].contains(expression))
                    return scope[i][expression]!!
            }
        }
        val tokens = parse(expression.substring(if(expression[1] == 'm') 6 else 5, expression.length -1))
        if(expression.startsWith("add", 1))
            return evaluate(tokens[0]) + evaluate(tokens[1])
        else if(expression.startsWith("mult", 1))
            return evaluate(tokens[0]) * evaluate(tokens[1])
        else {
            for(j in 1 until tokens.size step 2){
                scope[scope.size -1]!!.put(tokens[j-1], evaluate(tokens[j]))
            }
            return evaluate(tokens[tokens.size -1])
        }

    }
    fun parse(exp: String): List<String>{
        var res = mutableListOf<String>()
        var bal = 0
        var buf = StringBuilder()
        for(token in exp.split(" ")){
            for(c in token){
                if(c == '(') bal ++
                else if(c == ')') bal --
            }
            if(buf.length > 0) buf.append(" ")
            buf.append(token)
            if(bal == 0) {
                res.add(buf.toString())
                buf = StringBuilder()
            }
        }
        // if(buf.length > 0) res.add(buf.toString())
        return res
    }
}
