data class Money(
    var amount: Int,
    val currency: String
){
    override fun toString(): String{
        return currency + amount.toString()
    }
}
data class Customer(
    val name: String, 
    val cardNumber: String, 
    val limit: Money, 
    val balance: Money,
    val isValidCard: Boolean
    )
class Solution {
    val customers = hashMapOf<String, Customer>()
    fun validateCardNumber(cardNumber: String): Boolean{
        if(cardNumber.length !in 12 .. 16) return false
        return !cardNumber.map{it.isDigit()}.any{it == false} && checkLuhn(cardNumber)
    }
    fun checkLuhn(cardNumber: String): Boolean{
        var isSecond = false
        var total = 0
        for(i in cardNumber.length -1 downTo 0){
            var num = cardNumber[i].toInt() - '0'.toInt()
            // println("char is " + cardNumber[i] + " num is " + num)
            if(isSecond) num *= 2
            total += num / 10
            total += num % 10
            isSecond = !isSecond
        }
        println("luhn number for card " + cardNumber + " is " +total)
        return total % 10 == 0
    }
    fun stringToMoney(dollarAmount: String): Money{
        val currency = dollarAmount[0].toString()
        val amount = dollarAmount.substring(1).toInt()
        return Money(amount = amount, currency = currency)
    }
    fun validateCustomer(name: String): Boolean{
        if(customers[name] == null) {
            println("customer " + name + " cannot be found.")
            return false
        }
        val customer = customers[name]!!
        
        if(!customer.isValidCard){
            println("customer " + name + " card is invalid.")
            return false
        }
        return true
    }
    fun addBinary(a: String, b: String): String {
        val input = mutableListOf<List<String>>()
        input.add(listOf<String>("Add", "Tom", "4111111111111111", "$1000"))
        input.add(listOf<String>("Add", "Lisa", "5454545454545454", "$3000"))
        input.add(listOf<String>("Add", "Quincy", "12345678901234x", "$2000"))
        input.add(listOf<String>("Charge", "Tom", "$500"))
        input.add(listOf<String>("Charge", "Tom", "$800"))
        input.add(listOf<String>("Charge", "Lisa", "$7"))
        input.add(listOf<String>("Credit", "Lisa", "$100"))
        input.add(listOf<String>("Credit", "Quincy", "$200"))
        for(row in input){
            when(row[0]){
                "Add" -> {
                    val name = row[1]
                    val cardNumber = row[2]
                    val limitStr = row[3]
                    val isValidCard = validateCardNumber(cardNumber)
                    val limit = stringToMoney(limitStr)
                    val emptyBalance = Money(amount = 0, currency = "$")
                    val newCustomer = Customer(
                        name = name, 
                        cardNumber = cardNumber, 
                        limit = limit, 
                        balance = emptyBalance,
                        isValidCard = isValidCard
                        )
                    customers[name] = newCustomer
                }
                "Charge" -> {
                    val name = row[1]
                    val chargeStr = row[2]
                    val charge = stringToMoney(chargeStr)
                    if(!validateCustomer(name)) continue
                    val customer = customers[name]!!

                    val newBalance = charge.amount + customer.balance.amount
                    if(newBalance <= customer.limit.amount) {
                        customer.balance.amount = newBalance
                    } else println("customer " + customer.name +  " had charge over credit limit")
                }
                "Credit" -> {
                    val name = row[1]
                    val creditStr = row[2]
                    val credit = stringToMoney(creditStr)
                    if(!validateCustomer(name)) continue
                    val customer = customers[name]!!

                    val newBalance = customer.balance.amount - credit.amount
                    customer.balance.amount = newBalance
                }
            }
        }
        val res = mutableListOf<Customer>() 
        customers.forEach{it ->
            // println("customer " + it.key + " balance is " + it.value.balance.toString() +  " card validation " + it.value.isValidCard)
            res.add(it.value)
        }

        res.sortedBy{it.name }.forEach{
            println("customer " + it.name + " balance is " + it.balance.toString() +  " card validation " + it.isValidCard)
        }

        return ""
    }
}
