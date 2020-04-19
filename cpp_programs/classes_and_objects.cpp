#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cassert>
using namespace std;

class Student{
    public:
        int scores[5];
        void input()
        {
            for (int i=0;i<5;i++)
            {
                scanf("%d ",&scores[i]);
            }
        }
        int calculateTotalScore()
        {
            int sum=0;
            for (int i=0;i<5;i++)
            {
                sum+=scores[i];
            }
            return sum;
        }
};

int main() {