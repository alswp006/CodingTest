class Solution {
    fun solution(X: String, Y: String): String {
        var list = intArrayOf(0,0,0,0,0,0,0,0,0,0)
        var list2 = intArrayOf(0,0,0,0,0,0,0,0,0,0)
        var answer = StringBuilder()
        for(i in 0 until X.length){
            for(j in 0..9){
                if(X[i]==j.toChar()+48) {
                    list[j]+=1
                    break
                }
            }
        }
        for(i in 0 until Y.length){
            for(j in 0..9){
                if(Y[i]==j.toChar()+48) {
                    list2[j]+=1
                    break
                }
            }
        }
        for(i in 9 downTo 0){
            if(list[i]==0&&list2[i]==0) continue
            else if(list[i]<list2[i]){
                for(j in 1 .. list[i]){
                    answer.append(i)
                }
            }
            else{
                for(j in 1 .. list2[i]){
                    answer.append(i)
                }
            }
        }
        if(answer.length==0) return "-1"
        if(answer[0]=='0') return "0"
        return answer.toString()
    }
}