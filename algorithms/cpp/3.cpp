#include "iostream"
#include "string"
#include "map"
#include "iterator"
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
	if (s.size()<2)
	{
		return s.size();
	}
	int max_lenght = 0;
	int start = 0;
	map<char,int> dict;
	for(int i =0;i<s.size();i++)
	{
		map<char,int>::iterator iter = dict.find(s[i]);
		if(iter != dict.end())
		{
			start = max(start,dict[s[i]] + 1);
			dict[s[i]] = i;
		}
		else
		{
			dict[s[i]] = i;
		}
		max_lenght = max(max_lenght,i-start+1);
	}
	return max_lenght;
    }
};

int main(int argc, char const *argv[])
{
	string test = "abba";
	Solution *pObj = new Solution();
	cout<<pObj->lengthOfLongestSubstring(test)<<endl;
	delete pObj;
	return 0;
}