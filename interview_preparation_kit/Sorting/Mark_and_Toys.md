# Mark and Toys

## Link:
https://www.hackerrank.com/challenges/mark-and-toys/problem


## Explaination:
Sort then add toys in ascending order


## Code:

```
#include <algorithm>

int maximumToys(vector<int> prices, int k) {
    sort(prices.begin(), prices.end());
    int toy_cnt = 0;
    while (k - prices[toy_cnt] > 0) {
        k-= prices[toy_cnt];
        toy_cnt++;
    }
    return toy_cnt;
}


```
