import java.util.*;
class Solution {
    public int[] solution(int[] answers) {
    
        List<Integer> a = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5));
        List<Integer> b = new ArrayList<>(Arrays.asList(2, 1, 2, 3, 2, 4, 2, 5));
        List<Integer> c = new ArrayList<>(Arrays.asList(3, 3, 1, 1, 2, 2, 4, 4, 5, 5));
        
        // if answers의 길이가 a b c 각각의 길이보다 길면 answers의 길이 만큼 a,b,c 안에 들어있는 값을 반복해서 넣도록
        
        if(a.size() < answers.length) {
            while (a.size() < answers.length) {
                a.addAll(a); 
            }
        }
        if(b.size() < answers.length) {
            while (b.size() < answers.length) {
                b.addAll(b); 
            }
        }
        if(c.size() < answers.length) {
            while (c.size() < answers.length) {
                c.addAll(c); 
            }
        }
        
        int[] score = new int[3]; 
        
        for (int i = 0; i< answers.length; i++) {
            if(a.get(i) == answers[i]) score[0]++;
            if(b.get(i) == answers[i]) score[1]++;
            if(c.get(i) == answers[i]) score[2]++;
        }
        
        int maxScore = Math.max(score[0], Math.max(score[1], score[2]));
        
        
        List<Integer> list = new ArrayList<>();
        if (maxScore == score[0]) list.add(1);
        if (maxScore == score[1]) list.add(2);
        if (maxScore == score[2]) list.add(3);
    
        int[] answer = new int[list.size()]; // 1. 리스트 크기만큼 배열 생성

        for (int i = 0; i < list.size(); i++) {
            answer[i] = list.get(i);         // 2. 하나씩 꺼내서 옮겨 담기
        }    
        return answer;
    }
}