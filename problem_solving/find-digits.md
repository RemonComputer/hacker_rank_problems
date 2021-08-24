# Find-Digits

## Link:
https://www.hackerrank.com/challenges/find-digits/problem


## Explaination:
Simple divide and modulus understanding


## Code:

```
// This is the added code only

int findDigits(int n) {
    int t = n;
    int digit = 0;
    int cnt = 0;
    do{
        digit = t % 10;
        if(digit > 0 && (n % digit) == 0){
            cnt++;
        }
        t /= 10;
    }while(t > 0);
    return cnt;
}

```
