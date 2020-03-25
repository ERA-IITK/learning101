#include <iostream>
#include <string>
#include <sstream>
#include <exception>
using namespace std;

/* Define the exception here */
class BadLengthException : public  exception{
    public:
        int length;
        BadLengthException(int n)
        {
            length=n;
        }
        int what()
        {
            return length;
        }
        
};

