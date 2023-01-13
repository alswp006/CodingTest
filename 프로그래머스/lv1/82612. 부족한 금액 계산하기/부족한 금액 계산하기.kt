class Solution {
    fun solution(price: Int, money: Int, count: Int): Long {
        var sum : Long = 0L
        var a =1
        while(count!=a-1){
            sum += price.toLong()*a
            a+=1
        }
        return if(sum>money.toLong()) sum - money.toLong() else 0
    }
}