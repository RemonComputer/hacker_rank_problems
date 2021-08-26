# Merge-Two-Sorted-LinkeLists

## Link:
https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists/problem


## Explaination:
Merge-Two-Sorted-LinkeLists


## Code:

```
SinglyLinkedListNode* mergeLists(SinglyLinkedListNode* head1, SinglyLinkedListNode* head2) {
    if(head1 == nullptr){
        return head2;
    }
    if(head2 == nullptr){
        return head1;
    }
    SinglyLinkedListNode* current1 = head1, *current2 = head2;
    SinglyLinkedListNode* head = nullptr, *currentMain = nullptr, *tmp;
    while (current1 != nullptr && current2 != nullptr) {
        if (head == nullptr) {
            head = new SinglyLinkedListNode(0);
            currentMain = head;
        }else {
            SinglyLinkedListNode* newNode = new SinglyLinkedListNode(0);
            currentMain->next = newNode;
            currentMain = newNode;
        }
        if(current1->data > current2->data){
            currentMain->data = current2->data;
            tmp = current2->next;
            delete current2;
            current2 = tmp;
        }else {
            currentMain->data = current1->data;
            tmp = current1->next;
            delete current1;
            current1 = tmp;
        }
    }
    if(current1 != nullptr){
        currentMain->next = current1;
    }else if (current2 != nullptr) {
        currentMain->next = current2;
    }
    return head;
}


```
