import java.util.Arrays;
class Solution {
    public int solution(int[][] sizes) {
        int answer = 0;
        
        // 배열별로 가로랑 세로 비교해서 긴 쪽을 가로로 짧은 쪽으로 값 바꾸고
        
        for(int i = 0; i< sizes.length;i++) {
            if(sizes[i][0] <= sizes[i][1]) {
                int dum = sizes[i][0];
                sizes[i][0] = sizes[i][1];
                sizes[i][1] = dum;
            }
        }
        
        // System.out.println(Arrays.deepToString(sizes));
        
        int a = sizes[0][0];
        int b = sizes[0][1];
        
        // System.out.println(b);
        
        // 가로들만 보고 가장 큰 값이랑 세로 중에서 가장 큰 값
        for(int j = 1; j< sizes.length;j++) {
            if(a <= sizes[j][0]) {
                a = sizes[j][0];
            }
        }
        for(int k = 1; k< sizes.length;k++) {
            if (b <= sizes[k][1]) {
                b = sizes[k][1];
            }
        }
        return a*b;
    }
}


