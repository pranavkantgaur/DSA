'''
# https://leetcode.com/problems/reverse-linked-list/description/

Clarify:
1. All testcases reversible? yes
2. Empty list? No
3. In-place? yes
4. TC/SC? -> n, 1

Test-vcases"
1. [2, 1, 9, 3] -> [3, 9, 1, 2]
2. [2,2,2,2] -> [2,2,2,2]
3. [5, 8, 9, 2 .. 5000 elements] -> [ ... , , 2, 9, 8, 5]
4. [3, 5, 2, 1] -> [1, 2, 5, 3]
5. [-1, -5, -1] -> [-1, -5, -1]


Naive algorithm TC: o(n), SC-> O(n)
1. store all values of linked list in a list
2. reverse the list
3. Traverse the linked list again and overwrite each node value with that in the corresponding position in the list


Naive algo but inplace: TC: O(n^2), SC: O(1)
1. set left and right pointer to first and last node of linked list
2. swap their values
3. update left  =  left.next, relocate right = right of current right : O(n)
4. repeat 2 untill left < right


Bottlenecks:
1. Repetedly locating last pointer in the naive in-place algo is O(n)
2. Looking for an apporach which can flip the linked list during 1/2 passes over it

Approach:
1. Init last, current, next ptrs: last = null, current= head, next = head.next
2. if current.next = last, last = current, next.next = current, current = next, next ??

'''
