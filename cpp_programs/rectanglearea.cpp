#include <iostream>

using namespace std;
/*
 * Create classes Rectangle and RectangleArea
 */
 class Rectangle{
     public:
        int height,width;
        void display()
        {
            cout << height << " " << width << endl;
        }
 };
 class RectangleArea : public Rectangle{
     public:
        void read_input()
        {
            scanf("%d  %d",&height,&width);
        }
        void display()
        {
            cout << (height*width);
        }
 };

