/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

//  not done by me --yaswanth
class Solution {
public:
    ListNode* removeZeroSumSublists(ListNode* head) {
        if(head==NULL)return head;
        unordered_map<int,ListNode*>map;
        ListNode*dummy=new ListNode(0);
        dummy->next=head;
        map[0]=dummy;
        int preSum=0;
        while(head!=NULL){
             preSum+=head->val;
             if(map.find(preSum)!=map.end()){
               ListNode*start=map[preSum];
               int prevSum=preSum;
               while(start !=NULL && start!=head){
                start=start->next;
                prevSum+=start->val;
                if(start!=head){
                map.erase(prevSum);
                }
               }
               map[preSum]->next=start->next;
             }
             else{
                map[preSum]=head;
             }
                head=head->next;
        }
        return dummy->next;
    }
};