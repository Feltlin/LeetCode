/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode l3 = new ListNode();
        ListNode ptr = l3;
        int digit = 0, carry = 0;
        while(l1 != null || l2 != null || carry != 0){
            digit = carry;
            if(l1 != null){
                digit += l1.val;
                l1 = l1.next;
            }
            if(l2 != null){
                digit += l2.val;
                l2 = l2.next;
            }
            carry = digit / 10;
            digit %= 10;
            ptr.next = new ListNode(digit);
            ptr = ptr.next;
        }
        return l3.next;
    }
}