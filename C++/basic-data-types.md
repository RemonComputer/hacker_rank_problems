# Basic Data Types 

## Link:

https://www.hackerrank.com/challenges/c-tutorial-basic-data-types/problem?h_r=next-challenge&h_v=zen

## Explaination:

Read from input various datatypes and write it to output

## Code:

```

#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    // Complete the code.
    // int, long, char, float, and double
    int a;
    long b;
    char c;
    float f;
    double d;

    scanf("%d %ld %c %f %lf", &a, &b, &c, &f, &d);
    printf("%d\n%ld\n%c\n%f\n%lf", a, b, c, f, d);
    return 0;
}

```
