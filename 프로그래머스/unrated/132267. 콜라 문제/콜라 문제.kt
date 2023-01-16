class Solution {
    fun solution(a: Int, b: Int, n: Int): Int {
        var count = 0 
        var bottle = n
        while(bottle>=a){
              count+=bottle/a*b
            if(bottle/a==0) bottle=bottle/a*b
            else bottle=bottle/a*b+(bottle%a)
            }
        return count
    }
}