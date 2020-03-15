#include<bits/stdc++.h>

using namespace std;

class Box//Implement the class Box  
{
    private: int l,b,h;//l,b,h are integers representing the dimensions of the box
    // The class should have the following functions : 
    // Constructors: 
    public: Box()// Box();
    {
        l=b=h=0;
    }
    public: Box(int l,int b, int h)// Box(int,int,int);
    {
        this->l=l;
        this->b=b;
        this->h=h;
    }
    public: Box(Box& b)// Box(Box);
    {
        l=b.getLength();
        this->b=b.getBreadth();
        h=b.getHeight();
    }

    int getLength(){return l;}// int getLength(); // Return box's length
    int getBreadth(){return b;}// int getBreadth (); // Return box's breadth
    int getHeight(){return h;}// int getHeight ();  //Return box's height
    long long CalculateVolume()// long long CalculateVolume(); // Return the volume of the box
    {
        long long A=l*b;
        long long V=A*h;
        return V;
    }

//Overload operator < as specified
    bool operator<(Box& b)  
    {
        if(l<b.l)return true;
        else if(l==b.l&&this->b<b.b)return true;
        else if(l==b.l&&this->b==b.b&&h<b.h)return true;
        return false;
    }
};
//Overload operator << as specified
    ostream& operator<<(ostream& out, Box& B)
    {
        out<<B.getLength()<<' '<<B.getBreadth()<<' '<<B.getHeight();
        return out;
    }    



void check2()
{
	int n;
	cin>>n;
	Box temp;
	for(int i=0;i<n;i++)
	{
		int type;
		cin>>type;
		if(type ==1)
		{
			cout<<temp<<endl;
		}
		if(type == 2)
		{
			int l,b,h;
			cin>>l>>b>>h;
			Box NewBox(l,b,h);
			temp=NewBox;
			cout<<temp<<endl;
		}
		if(type==3)
		{
			int l,b,h;
			cin>>l>>b>>h;
			Box NewBox(l,b,h);
			if(NewBox<temp)
			{
				cout<<"Lesser\n";
			}
			else
			{
				cout<<"Greater\n";
			}
		}
		if(type==4)
		{
			cout<<temp.CalculateVolume()<<endl;
		}
		if(type==5)
		{
			Box NewBox(temp);
			cout<<NewBox<<endl;
		}

	}
}

int main()
{
	check2();
}