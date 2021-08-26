# MergeSort

## Link:
https://www.hackerrank.com/contests/hw1/challenges/merge-sort


## Explaination:
Implement Merge Sort


## Code:

```
void merge_sort(int arr[], int helper[], int start, int end){
    if(start >= end){
        return;
    }
    int middle = (start + end) / 2;
    merge_sort(arr, helper, start, middle);
    merge_sort(arr, helper, middle + 1, end);
    for(int i = start; i <= end; i++){
        // Copy array into helper;
        helper[i] = arr[i];
    }
    int i = start, j = middle + 1, main_idx = start;
    while(i <= middle && j <= end){
        if(helper[i] < helper[j]){
            arr[main_idx] = helper[i];
            i++;
        }else{
            arr[main_idx] = helper[j];
            j++;
        }
        main_idx++;
    }
    while(i <= middle){
        arr[main_idx] = helper[i];
        i++;
        main_idx++;
    }
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n;
    cin >> n;
    int array[n], helper[n];
    for(int i = 0; i < n; i++){
        cin >> array[i];
    }
    merge_sort(array, helper, 0, n - 1);
    cout << "[";
    for(int i = 0; i < n - 1; i++){
        cout << array[i] << ",";
    }
    cout << array[n - 1] << "]";
    return 0;
}



```
