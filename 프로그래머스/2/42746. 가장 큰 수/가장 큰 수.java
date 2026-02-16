import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        // String answer = "";
        // List<String> answer = new ArrayList<>();
        
        String[] nums = new String[numbers.length];
        
        // 일단 다 string으로 바꿈
        for(int i = 0; i< numbers.length; i++) {
            nums[i] = String.valueOf(numbers[i]);
        }
        //(a+b)랑 (b+a) 중에 뭐가 더 큰지 비교를 해봐야함
        Arrays.sort(nums, (a,b) -> (b+a).compareTo(a+b));
        
        if (nums[0].equals("0")) {
            return "0";
        }
        
        StringBuilder sb = new StringBuilder();
        for (String s : nums) {
            sb.append(s);
        }
        
        return sb.toString();
    }
}