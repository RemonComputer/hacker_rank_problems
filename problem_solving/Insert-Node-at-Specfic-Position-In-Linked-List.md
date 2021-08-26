# Insert-Node-at-Specfic-Position-In-Linked-List

## Link:
https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem


## Explaination:
Insert-Node-at-Specfic-Position-In-Linked-List


## Code:

```
SinglyLinkedListNode* insertNodeAtPosition(SinglyLinkedListNode* llist, int data, int position) {
    SinglyLinkedListNode* newNode = new SinglyLinkedListNode(data);
    if(position == 0){
        newNode->next = llist;
        return newNode;
    }
    SinglyLinkedListNode* currentNode = llist;
    for(int i = 1; i < position; i++){
        currentNode = currentNode->next;
    }
    newNode->next = currentNode->next;
    currentNode->next = newNode;
    return llist;
}


```
