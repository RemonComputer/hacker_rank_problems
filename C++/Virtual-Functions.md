# Virtual Functions

## Link:
https://www.hackerrank.com/challenges/virtual-functions/problem


## Explaination:
Check the main function code to understand how will you implement using virtual functions


## Code:

```

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

class Person{
    public:
        string name;
        int age;
    
    virtual void getdata() = 0;
    virtual void putdata() = 0;
    virtual void increment_id() = 0;
    
};

class Professor: public Person{
  public:
    int publications;
    int cur_id;
    static int next_cur_id;
    
    // Professor(){
    //     this->getdata();
    //     this->increment_id();
    // }
    
    virtual void increment_id(){
        next_cur_id++;
    }

    virtual void getdata(){
        cin >> this->name >> this->age >> this->publications;
        this->cur_id = next_cur_id;
        this->increment_id();
    }
    virtual void putdata(){
        cout << name << " " << age << " " << publications << " " << cur_id << endl;
    }
};

int Professor::next_cur_id = 1;

class Student: public Person{
    public:
        int marks[6];
        int cur_id;
        static int next_cur_id;
        
        // Student(){
        //     this->getdata();
        //     this->increment_id();
        // }
        
        virtual void increment_id(){
        next_cur_id++;
        }
        virtual void getdata(){
            cin >> this->name >> this->age;
            for(int i=0; i<6; i++){
                cin >> this->marks[i];
            }
            this->cur_id = next_cur_id;
            this->increment_id();
        }
        virtual void putdata(){
            int sum = 0;
            for(int i=0; i<6; i++){
                sum += this->marks[i];
            }
            cout << name << " " << age << " " << sum << " " << cur_id << endl;
        }
};

int Student::next_cur_id = 1;

int main(){

    int n, val;
    cin>>n; //The number of objects that is going to be created.
    Person *per[n];

    for(int i = 0;i < n;i++){

        cin>>val;
        if(val == 1){
            // If val is 1 current object is of type Professor
            per[i] = new Professor;

        }
        else per[i] = new Student; // Else the current object is of type Student

        per[i]->getdata(); // Get the data from the user.

    }

    for(int i=0;i<n;i++)
        per[i]->putdata(); // Print the required output for each object.

    return 0;

}


```
