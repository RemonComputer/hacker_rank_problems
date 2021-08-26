# QuickSort 2 - Sorting

## Link:
https://www.hackerrank.com/challenges/quicksort2/problem


## Explaination:
The full implementation of QuickSort.

Note: **The print is wrong bit the algorithm sorts successfully**


## Code:

```
void quick_sort(vector <int> &arr, int start, int end){
    if(start >= end){
        return;
    }
    //Partition
    int i = start + 1, j = end, pivot = arr[start], tmp;
    while (i <= j) {
        if(arr[i] <= pivot){
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
    arr[start] = arr[i];
    arr[i] = pivot;
    // cout << "pivot_idx: " << i << endl;
    // // Printing
    // for(int i = 0; i <= end; i++){
    //     cout << arr[i] << " ";
    // }
    // cout << "-------------------------" << endl;
    // divide recursive sort
    quick_sort(arr, start, i - 1);
    quick_sort(arr, i + 1, end);
    // Printing
    for(int i = start; i <= end; i++){
        cout << arr[i] << " ";
    }
    cout << endl;
}

void quickSort(vector <int> &arr) {
	// Complete this function
    quick_sort(arr, 0, arr.size() - 1);
}


```
