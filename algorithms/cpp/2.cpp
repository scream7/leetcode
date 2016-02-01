/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int carry = 0;
        int res = 0;
        ListNode *pHead = new ListNode(-1);
        ListNode *pCurNode = pHead;
        while(l1 != NULL || l2 != NULL || carry!=0)
        {
            res = 0;
            if(l1!=NULL)
            {
                res += l1->val;
                l1 = l1->next;
            }
            if(l2!=NULL)
            {
                res += l2->val;
                l2 = l2->next;
            }
            res += carry;
            if(res >9)
            {
                res -= 10;
                carry = 1;
            }
            else
            {
                carry = 0;
            }
            ListNode *pTmpNode = new ListNode(res);
            pCurNode->next = pTmpNode;
            pCurNode = pTmpNode;
        }
        return pHead->next;
    }
};
