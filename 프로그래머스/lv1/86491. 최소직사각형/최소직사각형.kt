class Solution {
    fun solution(sizes: Array<IntArray>): Int {
        for(i in 0 until sizes.size){
            if(sizes[i][0] < sizes[i][1]){
                var a = sizes[i][0]
                sizes[i][0] = sizes[i][1]
                sizes[i][1] = a
            }
        }
        
        var b = sizes[0][0]
        var c = sizes[0][1]
        
        for ( i in 1 until sizes.size) {
            if(b<sizes[i][0]){
                b = sizes[i][0]
            }
            if(c<sizes[i][1]){
                c = sizes[i][1]
            }
        }
        
        var answer: Int = 0
        return b*c
    }
}