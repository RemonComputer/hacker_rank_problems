# Print-Elements-of-Linked-List

## Link:
https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list/problem


## Explaination:
Print elements of linked list.


## Code:

```
void printLinkedList(SinglyLinkedListNode* head) {
    while(head != nullptr){
        cout << head->data << endl;
        head = head->next;        
    };

}
```
