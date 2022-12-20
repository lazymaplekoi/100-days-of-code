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
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2) {
        ListNode sum = new ListNode();
        ListNode temp = new ListNode();

        var (value, carryOver) = AddNodes(l1, l2, 0, 0);
        sum.val = value;

        if (l1.next == null && l2.next == null)
        {
            if (carryOver > 0) sum.next = new ListNode(carryOver);
            return sum;
        }

        l1 = l1.next;
        l2 = l2.next;
        sum.next = temp;

        while (l1 != null || l2 != null)
        {
            if (l1 == null) l1 = new ListNode();
            if (l2 == null) l2 = new ListNode();
        
            (value, carryOver) = AddNodes(l1, l2, value, carryOver);

            temp.val = value;

            l1 = l1.next;
            l2 = l2.next;

            if (carryOver > 0) temp.next = new ListNode(carryOver);
            if (l1 == null && l2 == null) break;

            temp.next = new ListNode();
            temp = temp.next;
        }

        return sum;
    }

    public (int, int) AddNodes(ListNode l1, ListNode l2, int value, int carryOver)
    {
        value = l1.val + l2.val + carryOver;

        return value > 9 ?
            (value - 10, 1) :
            (value     , 0);
    }

    private string PrintListNode(ListNode node)
    {
        var ptr = node;
        var builder = new StringBuilder();
        while (ptr != null)
        {
            builder.Append($"({ptr.val})");
            if (ptr.next != null) builder.Append("->");
            ptr = ptr.next; 
        }

        return builder.ToString();
    }
}