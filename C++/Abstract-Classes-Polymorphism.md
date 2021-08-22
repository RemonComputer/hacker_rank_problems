# Abstract Classes - Polymorphism

## Link:
https://www.hackerrank.com/challenges/abstract-classes-polymorphism/problem



## Explaination:
Check if the key exits in the cache then rewire the node, otherwise add a new node at the head and remove extra node if you exceeded the capacity, there is also a very special case in which you are always hitting the head node


## Code:

```
// This is the added code only
class LRUCache: public Cache{
    public:
    int default_hit_key;
    
    LRUCache(int capacity){
        this->cp = capacity;
        this->tail = NULL;
        this->head = NULL;
        this->default_hit_key = -1;
    }
    
    void print_status(){
        cout << "cp: " << cp << endl;
        if(head != NULL){
            cout << "head: " << "(" << head->key << ", " << head ->value << ")" << endl;
        }else {
            cout << "head: NULL" << endl;
        }
        if(tail != NULL){
            cout << "tail: " << "(" << tail->key << ", " << tail ->value << ")" << endl;
        }else {
            cout << "tail: NULL" << endl;
        }
        Node* current = tail;
        cout << "Linked List: ";
        while (current != NULL) {
            cout << "(" << current->key << ", " << current->value << "), ";
            current = current->next; 
        }
        cout << endl;
        cout << "-----------------------" << endl;
    }
    virtual int get(int key){
        //print_status();
        if(head != NULL && head->key == key){
            // Very Special case
            return head->value;
        }
        // Check if it originally existed in the cache
        auto found_itr = this->mp.find(key);
        if(found_itr != this->mp.end()){
            // // The key was originally in the cache
            // n->value = found_itr->second->value;
            // //Delete the old node
            // found_itr->second->next->prev = found_itr->second->prev;
            // if(found_itr->second->prev == NULL){
            //     // I am in the tail pointer, So advance the tail pointer
            //     this->tail = this->tail->next;
            // }else{
            //     // I am in the middle of the list
            //     found_itr->second->prev->next = found_itr->second->next;
            // }
            // //Delete the node from mp
            // mp.erase(found_itr);
            // // Release the memory of the old node
            // delete found_itr->second;
            
            // connecting the next node
            found_itr->second->next->prev = found_itr->second->prev;
            if(found_itr->second->prev != NULL){
                // In the middle of the list
                found_itr->second->prev->next = found_itr->second->next;
            }else{
                // I am in the tail node
                tail = tail->next;
            }
            // connect this node infront of the head and modify the head
            head->next = found_itr->second;
            found_itr->second->prev = head;
            // Advance the head pointer
            head = head->next;
        }else{
            // Create a new Node
            Node* n = new Node(key, this->default_hit_key);
            //Place the node at the front of the linked list
            n->prev = this->head;
            if(this->head != NULL){
                this->head->next = n;
            }else{
                tail = n;
            }
            // Setting of the head
            head = n;
                if(mp.size() >= cp){
                // The key was not in the cache and we would exceed the capacity
                // So we need to delete the old tail and advance the pointer
                Node* old_tail = tail;
                // Advance the tail pointer
                tail = tail->next;
                // Delete the old tail from mp
                mp.erase(old_tail->key);
                // Release the memory of the old node
                delete old_tail;
                }
            // Add the new node to mp
            mp.insert(make_pair(key, n));
        }
        return head->value;
    }
    
    virtual void set(int key, int val){
        get(key);
        head->value = val;
    }
    
};


```
