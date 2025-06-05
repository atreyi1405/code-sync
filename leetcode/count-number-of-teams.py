class Solution {
    public int numTeams(int[] rating) {
        int res=0;
        for(int j=1; j<rating.length; j++){
            int leftsmaller=0;
            int leftgreater=0;
            int rightsmaller=0;
            int rightgreater=0;
            for(int i=0; i<j; i++){
                if(rating[i]<rating[j]){
                    leftsmaller++;
                }else{
                    leftgreater++;
                }
            }
            for(int k=j+1; k<rating.length; k++){
                if(rating[k]<rating[j]){
                    rightsmaller++;
                }
                else{
                    rightgreater++;
                }
            }
            res+= leftsmaller*rightgreater + rightsmaller*leftgreater;

        }
        return res;
    }
}