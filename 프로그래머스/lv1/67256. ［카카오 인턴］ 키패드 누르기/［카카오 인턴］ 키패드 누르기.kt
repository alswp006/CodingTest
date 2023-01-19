import kotlin.math.*

class Solution {
    fun solution(numbers: IntArray, hand: String): String {
    var answer = ""
    var arr = arrayOf(arrayOf(1,1),arrayOf(2,1),arrayOf(3,1),
                     arrayOf(4,2),arrayOf(5,2),arrayOf(6,2),
                     arrayOf(7,3),arrayOf(8,3),arrayOf(9,3),
                     arrayOf(10,4),arrayOf(11,4),arrayOf(12,4))
    var left = arr[9]
    var right = arr[11]
    for(i in 0 until numbers.size){
        if(numbers[i]==0) numbers[i]=11
        if(numbers[i]==1||numbers[i]==4||numbers[i]==7){
            answer+='L'
            left = arr[numbers[i]-1]
        }
        else if(numbers[i]==3||numbers[i]==6||numbers[i]==9){
            answer+='R'
            right = arr[numbers[i]-1]
        }
        else{
            var num = arr[numbers[i]-1]
            var ll = 0
            var rr = 0
              if(abs(left[0]-num[0])!=3&&abs(left[0]-num[0])!=6&&abs(left[0]-num[0])!=9){
            	if(num[0]<left[0]){
                    if(abs(num[0]-left[0])==4||abs(num[0]-left[0])==2) ll=2
                    else if (abs(num[0]-left[0])==7) ll=3
                    else ll+=(left[0]-1)/3+1
                } 
            	else if(num[0]>left[0]) {
            	    if(num[1]==left[1]) ll=1
            	    else {
                        if(abs(num[0]-left[0])==4||abs(num[0]-left[0])==2) ll=2
                    	else if (abs(num[0]-left[0])==7) ll=3
                        else ll+=(num[0]-1)/3+1
                    }
                }
            	else ll=0             
            }
            else ll=abs(left[1]-num[1])	
            if(abs(right[0]-num[0])!=3&&abs(right[0]-num[0])!=6&&abs(right[0]-num[0])!=9){
            	if(num[0]<right[0]){
            	    if(num[1]==right[1]) rr=1
            	    else{
                        if(abs(num[0]-right[0])==4||abs(num[0]-right[0])==2) rr=2
                    	else if (abs(num[0]-right[0])==5) rr=3
                        else rr+=(right[0]-1)/3+1
                    } 
            	}
                else if(num[0]>right[0]){
                    if(abs(num[0]-right[0])==4||abs(num[0]-right[0])==2) rr=2
                    else if (abs(num[0]-right[0])==5) rr=3
                    else rr+=(num[0]-1)/3+1
                } 
                else rr=0
        	}
            else rr=abs(right[1]-num[1])
            if(rr>ll){
                left = num
                answer+='L'
            }
            else if(rr<ll){
                right = num
                answer+='R'
            }
            else{
                if(hand=="right"){
                    right = num
                	answer+='R'
                }
                else{
                    left = num
                	answer+='L'
                }
            }
        }
    }
    return answer
    }
}