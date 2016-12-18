public class Solution {
    public int[] twoSum(int[] numbers, int target) {
        
        // sorted way
        int[] res = new int[2];
        int l = 0, r = numbers.length-1;
        while (l < r){
            if(numbers[l] + numbers[r] > target)
                r--;
            else if(numbers[l] + numbers[r] < target)
                l++;
            else{
                res[0] = l+1;
                res[1] = r+1;
                break;
            }
        }
        return res;
        // #unsorted way
        // # res = []
        // # dic = {}
        // # for i in xrange(len(numbers)):
        // #     if target - numbers[i] in dic:
        // #         res.append(dic[target-numbers[i]])
        // #         res.append(i+1)
        // #         break
        // #     else:
        // #         dic[numbers[i]] = i+1
            
        // # return res
    }
}