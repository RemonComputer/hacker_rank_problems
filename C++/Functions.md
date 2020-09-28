# Functions
 

## Link:

https://www.hackerrank.com/challenges/c-tutorial-functions/problem

## Explaination:

Finding the max of four numbers using max

## Code:

```

#include <iostream>
#include <cstdio>
using namespace std;

/*
Add `int max_of_four(int a, int b, int c, int d)` here.
*/
int max_of_four(int a, int b, int c, int d){
    int arr[] = {a, b, c, d};
    int max_el = arr[0];
    for(int i=1; i<4; i++){
        if(arr[i] > max_el){
            max_el = arr[i];
        }
    }
    return max_el;
}

int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}


```
