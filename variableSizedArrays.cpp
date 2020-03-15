#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    int n, q;
    cin >> n >> q;
    int **list = new int*[n];
    for(int i = 0; i < n; i++) {
        int k;
        cin >> k;
        list[i] = new int[k];
        for(int j = 0; j < k; j++) {
            int x;
            cin >> x;
            list[i][j] = x;
        }
    }
    for(int i = 0; i < q; i++) {
        int a, b;
        cin >> a >> b;
        cout << list[a][b] << endl;
    }
       
    return 0;
}
