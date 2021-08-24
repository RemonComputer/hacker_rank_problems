# Array Manipulation

## Link: 
https://www.hackerrank.com/challenges/crush/problem



## Explaination:
**Warning** 7/16 failed due to time limit and the 1/16 due to wrong answer.

Implemented splitting of the boundaries using a list of boundaries


## Code:

```
struct ArrayArea{
    int left_idx, right_idx; 
    long max_val;
    ArrayArea(int l, int r, long v): left_idx(l), right_idx(r), max_val(v){
        
    }
};

// vector<int> get_effected_areas_idxs(int a, int b, const vector<ArrayArea>& areas){
//     vector<int> idxs;
//     for(int i = 0; i < areas.size(); i++){
//         auto& current_area = areas[i];
//         bool cond1 = (a >= current_area.left_idx) && (a <= current_area.right_idx);
//         bool cond2 = (b >= current_area.left_idx) && (b <= current_area.right_idx);
//         bool cond3 = (current_area.left_idx >= a) && (current_area.left_idx <= b);
//         if(cond1 || cond2 || cond3){
//             idxs.push_back(i);
//         }
//     }
//     return idxs;
// }

void print_areas(list<ArrayArea*>& areas){
    for(auto i = areas.begin(); i != areas.end(); i++){
        cout << "left_idx: " << (*i)->left_idx << ", ";
        cout << "right_idx: " << (*i)->right_idx << ", "; 
        cout << "max val: " << (*i)->max_val << endl;
    }
}

void print_one_area(ArrayArea* a){
    cout << "left_idx: " << a->left_idx << ", ";
        cout << "right_idx: " << a->right_idx << ", "; 
        cout << "max val: " << a->max_val << endl;
}

void modify_array_areas(int a, int b, long k, list<ArrayArea*>& areas){
    ArrayArea* current_area;
    for(auto i = areas.begin(); i != areas.end(); i++){
        current_area = *i;
        //print_one_area(current_area);
        if(a <= current_area->left_idx && b >= current_area->right_idx){
            // cout << "case 1:"<< endl;
            current_area->max_val += k;
            if(b == current_area->right_idx){
                break;
            }
        }else if(a > current_area->left_idx && a <= current_area->right_idx){
            // cout << "a: " << a << endl;
            // Divide to make a new area
            ArrayArea* newArea = new ArrayArea(a, current_area->right_idx, current_area->max_val);
            areas.insert(++i, newArea);
            --(--i);
            // Modify the old area boundaries
            current_area->right_idx = a - 1;
            // cout << "case 2:" << endl; 
        }else if(b > current_area->left_idx && b <= current_area->right_idx){
            // Divide to make a new area
            ArrayArea* newArea =  new ArrayArea(b + 1, current_area->right_idx, current_area->max_val);
            areas.insert(++i, newArea);
            // Modify old area boundaries
            current_area->right_idx = b;
            // (--(--i));
            (--(--i));
            // cout << "case 3:" << endl;
            current_area->max_val += k;
            break;
        }
        //print_areas(areas);
        // cout  << "--------------" << endl;
    }
}
long arrayManipulation(int n, vector<vector<int>> queries) {
    list<ArrayArea*> areas;
    areas.push_back(new ArrayArea(1, n, 0));
    // Begin alogrithm
    int a, b, k;
    for(auto& q:queries){
        a = q[0];
        b = q[1];
        k = q[2];
        //cout << "--------------------" << endl;
        //cout << "a: " << a << ", b: " << b << ", k:" << k << endl;
        //cout << "--------------------" << endl;
        modify_array_areas(a, b, k, areas);
    }
    long max_val = 0;
    for(auto i = areas.begin(); i != areas.end(); i++){
        if(max_val < (*i)->max_val){
            max_val = (*i)->max_val;
        }
    }
    //print_areas(areas);
    return max_val;
}


```
