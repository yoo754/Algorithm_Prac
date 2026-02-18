import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        // int[] answer = {};
        ArrayList<Integer> list = new ArrayList<>(); // answer 전단계로 넣을곳
        
        
        int idx = 0;

        while(idx < progresses.length) {
            int cnt = 0;
            // 1.업무
            
            for (int i = 0; i<progresses.length; i++) {
                progresses[i] += speeds[i];
                }
            
            // 2. 배포 가능한지 확인:
            while(idx < progresses.length && progresses[idx] >= 100) {
                cnt++;   // 배포 개수 추가
                idx++; // 다음 타자로 포인터 이동 (이제 이 친구가 맨 앞)
            }

            // 3. 만약 오늘 배포된 게 있다면(cnt > 0), list에 추가
            if(cnt > 0) {
                list.add(cnt);
            }
            }
        
        int[] answer = new int[list.size()];
        
        for(int j = 0; j< list.size(); j++) {
            answer[j] = list.get(j);
        }
            
        
        return answer;
    }
}