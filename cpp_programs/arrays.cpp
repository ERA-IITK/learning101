#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n;
    scanf("%d\n",&n);
    int a[n];
    for (int i=0;i<n;i++)
        scanf("%d",&a[i]);
    for (int i=n-1;i>=0;i--)
        printf("%d ",a[i]);
    return 0;
}
