class Solution {
    fun solution(N: Int, stages: IntArray): IntArray {
        var answer = intArrayOf()
        var a = 0.0
        var num = stages.size.toDouble()
        var ratio : MutableMap<Int,Double> = mutableMapOf()
        for(i in 0 until N){
            a = stages.count{it==i+1}.toDouble()
            ratio.put(i+1,a/(num))
            num-=a
            if(num==0.0) num =1.0
        }
        var mapList = ratio.toList().sortedByDescending{it.second}
        for(i in mapList.iterator()) answer = answer.plus(i.first)
        return answer
    }
}