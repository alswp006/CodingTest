class Solution {
    fun solution(n: Int): Int {
        var fibo = mutableListOf<Int>(0,1)
        for(i in 1 .. n){
            fibo.add((fibo[i-1]+fibo[i])%1234567)
        }
        return fibo[n]
    }
}