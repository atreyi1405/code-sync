class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        HashSet<Integer> set=new HashSet<>();
        for(int num:nums1){
            set.add(num);
        }

        HashSet<Integer> result=new HashSet<>();
        for(int num2:nums2){
            if(set.contains(num2)){
                //if common element then add to result
                result.add(num2);
            }
        }
        //now result to array
        int j=0;
        int[] res= new int[result.size()];
        for(int number:result){
            res[j++]=number;
        }
        return res;
        
    }
}