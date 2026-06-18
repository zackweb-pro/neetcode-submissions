class Solution {
public:
    int maxArea(vector<int>& heights) {
        int l = 0;
        int r = (int)heights.size();
        r--;
        int curr = 0;
        int max_val = 0;
        while(l<r){
            curr = (r-l)*(heights[l] < heights[r]? heights[l]:heights[r]);
            heights[l]<heights[r] ? l++: r--;
            max_val= (curr > max_val ? curr : max_val);
        }
        return max_val;
    }
};
