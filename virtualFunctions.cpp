#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
class Person
{   
    public:
    string name;
    int age;
    virtual void getdata()=0;
    virtual void putdata()=0;
};
class Professor:public Person
{
    private:
    static int count;
    public:
    int publish;
    void getdata()
    {
        cin>>name;
        cin>>age;
        cin>>publish;
        count=0;
    }
    void putdata()
    {
        int curr=++count;
        cout<<name<<' '<<age<<' '<<publish<<' '<<curr<<'\n';
    }
};
int Professor::count;
class Student:public Person
{
    private:
            static int count;
    public:
    int total;
    void getdata()
    {
        cin>>name;
        cin>>age;
        count=0;
        for(int x=0; x<6; x++)
        {
            int n;
            cin>>n;
            total=total+n;
        }
    }
    void putdata()
    {
        int curr=++count;
        cout<<name<<' '<<age<<' '<<total<<' '<<curr<<'\n';
    }
};
int Student::count;
int main(){

    int n, val;
    cin>>n; //The number of objects that is going to be created.
    Person *per[n];

    for(int i = 0;i < n;i++){

        cin>>val;
        if(val == 1){
            // If val is 1 current object is of type Professor
            per[i] = new Professor;

        }
        else per[i] = new Student; // Else the current object is of type Student

        per[i]->getdata(); // Get the data from the user.

    }

    for(int i=0;i<n;i++)
        per[i]->putdata(); // Print the required output for each object.

    return 0;

}
