# Pointers 

## Link:

https://www.hackerrank.com/challenges/c-tutorial-pointer/problem

## Explaination:

Practice Pointers by modifying the values through pointers that points to the values

## Code:

```

#include <stdio.h>

void update(int *a,int *b) {
    // Complete this function
    int a_dash, b_dash;
    a_dash = *a + *b;
    if(*a > *b){
        b_dash = *a - *b;
    }else{
        b_dash = *b - *a;
    }
    *a = a_dash;
    *b = b_dash;
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}

```
