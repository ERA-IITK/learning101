#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <set>
#include <cassert>
using namespace std;

struct Node{
   Node* next;
   Node* prev;
   int value;
   int key;
   Node(Node* p, Node* n, int k, int val):prev(p),next(n),key(k),value(val){};
   Node(int k, int val):prev(NULL),next(NULL),key(k),value(val){};
};

class Cache{
   
   protected: 
   map<int,Node*> mp; //map the key to the node in the linked list
   int cp;  //capacity
   Node* tail; // double linked list tail pointer
   Node* head; // double linked list head pointer
   virtual void set(int, int) = 0; //set function
   virtual int get(int) = 0; //get function

};
class LRUCache: public Cache
{   
    public:
    LRUCache(int cap)
    {
        cp=cap;
        head=NULL;
        tail=NULL;
        //cout<<cap;
    }
    void set(int k,int v)
    {
        if(head==NULL)
        {
            head=new Node(k, v);
            return;
            //cout<<head->key<<' '<<head->value;
        }
        Node* curr=head;
        while(curr!=NULL)
        {

            //cout<<curr->key;
            if(k==curr->key)
            {                
                if(curr->prev!=NULL)
                {   
                    //cout<<curr->prev->key<<'\n';
                    if(curr->next!=NULL)curr->prev->next=curr->next;
                    else curr->prev->next=NULL;
                    //cout<<curr->prev->next->key<<'\n';
                    if(curr->next!=NULL)
                    {   
                        //cout<<curr->next->key<<'\n';
                        curr->next->prev=curr->prev;
                        //cout<<curr->next->prev->key<<'\n';
                    }
                }
                break;
            }
            curr=curr->next;
        }
        /*Node *newNode=(struct*Node)malloc(sizeOf(struct Node));
        newNode->prev=NULL;
        newNode->next=head;*/
        Node *newNode= new Node(NULL,head,k,v);
        head->prev=newNode;
        head=newNode;
        //display();
    }
    int get(int k)
    {
        Node* curr=head;
        //cout<<'k'<<curr->key<<'\n';
        for(int x=0; x<cp; x++)
        {
            if(curr==NULL)return -1;
            if(curr->key==k)
            {
                int i=curr->value;
                if(curr->prev!=NULL)
                {   
                    //cout<<curr->prev->key<<'\n';
                    if(curr->next!=NULL)curr->prev->next=curr->next;
                    else curr->prev->next=NULL;
                    //cout<<curr->prev->next->key<<'\n';
                    if(curr->next!=NULL)
                    {   
                        //cout<<curr->next->key<<'\n';
                        curr->next->prev=curr->prev;
                        //cout<<curr->next->prev->key<<'\n';
                    }
                    curr->next=head;
                    curr->prev=NULL;
                    head->prev=curr;
                    head=curr;
                    //display();
                }
                 //display();
                return i;
            }
            curr=curr->next;
        }
        return -1;
    }
    void display()
    {
        Node* curr=head;
        while(curr!=NULL)
        {
            cout<<curr->key<<' ';
            curr=curr->next;
        }
        cout<<'\n';
    }
};  
int main() {
   int n, capacity,i;
   cin >> n >> capacity;
   LRUCache l(capacity);
   for(i=0;i<n;i++) {
      string command;
      cin >> command;
      if(command == "get") {
         int key;
         cin >> key;
         cout << l.get(key) << endl;
      } 
      else if(command == "set") {
         int key, value;
         cin >> key >> value;
         l.set(key,value);
      }
   }
   return 0;
}
