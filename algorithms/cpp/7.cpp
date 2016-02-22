class Solution {
public:
    int reverse(int x) {
        if (0 == x)
        {
            return 0;
        }
        long long int res = 0;
        int sign = x > 0 ? 1:-1;
        x = abs(x);
        while(x)
        {
            res *= 10;
            res += x%10;
            x /= 10;
        }
        if((res > INT_MAX)  || (res < INT_MIN))
        {
            return 0;
        }
        return res * sign;
    }
};