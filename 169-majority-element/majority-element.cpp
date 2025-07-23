class Solution
{
    public:
        int majorityElement(vector<int> &nums)
        {
            int n = nums.size();
            map<int, int> m;
            for (int i = 0; i < n; i++)
            {
                m[nums[i]]++;
            }
            int f = n / 2;
            int ans;

            for (auto it: m)
            {
                if (it.second > f) {
                    ans=it.first;
                }
            }
            return ans;
        }
};
  