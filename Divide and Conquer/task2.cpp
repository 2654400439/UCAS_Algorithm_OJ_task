#include <iostream>
#include <stdio.h>
using namespace std;
const int maxn = 1e8 + 1e2;
const int maxt = 1e5 + 1e2;
int arr[maxn];
int aim[maxt];

int binary_find(int type, int left, int right, int aim) {
    int mid;
    while(left <= right){
        mid = (left + right) / 2;
        // printf("left = %d, right = %d, mid = %d\n", left, right, mid);
        if(arr[mid] < aim) {
            left = mid + 1;
        } else if(arr[mid] > aim) {
            right = mid - 1;
        } else if(arr[mid] == aim) {
            if(type == 0) {
                // find min index -> left
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
    }
    int resIndex;

    if(type == 0) {
        resIndex = right + 1;
    } else {
        resIndex = left - 1;
    }
    // printf("resIndex = %d\n", resIndex);

    if(arr[resIndex] != aim) {
        return -1;
    } else {
        return resIndex;
    }

}

int main()
{
    int n, t;
    scanf("%d%d",&n, &t);
    for(int i = 0; i < n; ++i) {
        scanf("%d", &arr[i]);
    }
    for(int i = 0; i < t; ++i) {
        scanf("%d", &aim[i]);
    }
    for(int i = 0; i < t; ++i) {
        int left = 0, right = n - 1;
        int low_idx = binary_find(0, 0, right, aim[i]);
        int up_idx = binary_find(1, 0, right, aim[i]);
        printf("%d %d\n", low_idx, up_idx);
    }
    return 0;
}
