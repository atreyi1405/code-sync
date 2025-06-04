class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length == 0) {
            return 0; //empty
        }
        
        int j = 1; 
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != nums[i - 1]) { //found unique element
                nums[j] = nums[i]; 
                j++;
            }
        }
        return j;
    }
}