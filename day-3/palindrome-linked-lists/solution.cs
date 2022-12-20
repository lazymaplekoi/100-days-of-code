/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public bool IsPalindrome(ListNode head) 
    {
        var stackOne = new Stack<int>();
        var stackTwo = new Stack<int>();
        int len = 0;
        
        while (head != null)
        {
            stackOne.Push(head.val);
            head = head.next;
        }

        len = stackOne.Count;

        if (len == 1) return true;

        while (stackOne.Any() && stackTwo.Count < len / 2)
        {
            stackTwo.Push(stackOne.Pop());
        }

        if (len % 2 != 0) stackOne.Pop();

        while (stackOne.Count > 0 && stackTwo.Count > 0)
        {
            if (stackOne.Pop() != stackTwo.Pop()) return false;
        }

        return !stackOne.Any() && !stackTwo.Any();
    }
}