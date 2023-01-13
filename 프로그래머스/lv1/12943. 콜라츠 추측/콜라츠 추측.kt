class Solution {
    fun solution(num: Int): Int {
        var a = 0
        var input:Long = num.toLong()
        while(input!=1L||a==500){
            if(input%2L==0L){
                input/=2L
            }
            else{
                input=input*3L+1L
            }
            a+=1
        }
        return if(a<500){a}else{-1}
    }
}