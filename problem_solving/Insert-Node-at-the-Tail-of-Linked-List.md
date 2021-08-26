# Insert Node at the tail of linked list

## Link:
https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list/problem


## Explaination:
Insert Node at the tail of linked list


## Code:

```
SinglyLinkedListNode* insertNodeAtTail(SinglyLinkedListNode* head, int data) {
    if(head == nullptr){
        SinglyLinkedListNode* n = new SinglyLinkedListNode(data);
        return n;
    }
    SinglyLinkedListNode* current = head;
    while (current->next != nullptr) {
        current = current->next;
    }
    current->next = new SinglyLinkedListNode(data);
    return head;
}


```
