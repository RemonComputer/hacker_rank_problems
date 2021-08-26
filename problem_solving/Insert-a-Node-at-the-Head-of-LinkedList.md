# Insert-a-Node-at-the-Head-of-LinkedList

## Link:
https://www.hackerrank.com/challenges/insert-a-node-at-the-head-of-a-linked-list/problem


## Explaination:
Insert-a-Node-at-the-Head-of-LinkedList


## Code:

```
SinglyLinkedListNode* insertNodeAtHead(SinglyLinkedListNode* llist, int data) {
    SinglyLinkedListNode* newHead = new SinglyLinkedListNode(data);
    newHead->next = llist;
    return newHead;
}


```
