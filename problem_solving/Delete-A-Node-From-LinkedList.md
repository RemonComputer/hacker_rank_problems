# Delete-A-Node-From-LinkedList

## Link:
https://www.hackerrank.com/challenges/delete-a-node-from-a-linked-list/problem


## Explaination:
Delete-A-Node-From-LinkedList


## Code:

```
SinglyLinkedListNode* deleteNode(SinglyLinkedListNode* llist, int position) {
    if(position == 0){
        SinglyLinkedListNode* newHead = llist->next;
        delete llist;
        return newHead;
    }
    SinglyLinkedListNode* current = llist;
    for(int i = 1; i < position; i++){
        current = current->next;
    }
    SinglyLinkedListNode* nextNode = current->next->next;
    delete current->next;
    current->next = nextNode;
    return llist;
}


```
