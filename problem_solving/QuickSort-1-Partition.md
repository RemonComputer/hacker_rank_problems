# QuickSort-1-Partition

## Link:
https://www.hackerrank.com/challenges/quicksort1/problem


## Explaination:
QuickSort-1-Partition


## Code:

```
vector<int> quickSort(vector<int> arr) {
    int pivot = arr[0];
    int i = 1, j = arr.size() - 1, tmp;
    while(i <= j){
        //cout << i << ", " << j << endl;
        if(arr[i] <= pivot){  // or "<" only
            i++;
            continue;
        }
        if(arr[j] > pivot){
            j--;
            continue;
        }
        tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
        i++;
        j--;
    }
    i--;
    arr[0] = arr[i];
    arr[i] = pivot;
    return arr;
}


```
