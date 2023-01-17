class Solution {
    fun solution(n: Int, lost: IntArray, reserve: IntArray): Int {
        var answer = 0
        var list = mutableListOf<Int>()
        var finallist  = mutableListOf<Int>()
        var losts = lost.sortedArray().toMutableList()
        var reserves = reserve.sortedArray().toMutableList()
        for(i in 0 until reserves.size){
            if(losts.contains(reserves[i])) {
                list.add(reserves[i])
                losts.remove(reserves[i])
            }
            else if(losts.contains(reserves[i]-1)){
                if(list.size>=1&&list[0]==reserves[i]-1) list.add(reserves[i]+1)
                else list.add(reserves[i]-1)}
            else if(losts.contains(reserves[i]+1)) list.add(reserves[i]+1)
        }
        var ml = list.distinct()
        for(i in 0 until ml.size){
            if(lost.contains(ml[i])) finallist.add(ml[i])
        }
        if(ml.size>lost.size) answer=n
        else answer = n-lost.size+finallist.size
        return answer
    }
}