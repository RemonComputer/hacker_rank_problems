# Box It 

## Link: 

https://www.hackerrank.com/challenges/box-it/problem

## Explaination:

Basic Class + Operator Overloading + Stream operator Overloading + casting to long

## Code:

```

#include<bits/stdc++.h>

using namespace std;
//Implement the class Box  
//l,b,h are integers representing the dimensions of the box

// The class should have the following functions : 

// Constructors: 
// Box();
// Box(int,int,int);
// Box(Box);


// int getLength(); // Return box's length
// int getBreadth (); // Return box's breadth
// int getHeight ();  //Return box's height
// long long CalculateVolume(); // Return the volume of the box

//Overload operator < as specified
//bool operator<(Box& b)

//Overload operator << as specified
//ostream& operator<<(ostream& out, Box& B)

class Box{
    private:
    int l;
    int b;
    int h;

    public:
        Box(int length=0, int breadth=0, int height=0):l(length), b(breadth), h(height){
        }

        Box(Box& anotherBox){
            l = anotherBox.l;
            b = anotherBox.b;
            h = anotherBox.h;
        }

        bool operator<(Box& anotherBox){
            // if(this->l < anotherBox.l || ){
            //     return true;
            // }
            // return false;
            return (this->l < anotherBox.l) || (this->l == anotherBox.l && this->b < anotherBox.b) ||(this->l == anotherBox.l && this->b == anotherBox.b && this->h < anotherBox.h);
        }

        friend ostream& operator<<(ostream& stream, Box& b){
            stream << b.l << " " << b.b << " " << b.h;
            return stream;
        }

        int getLength(){
            return this->l;
        }

        int getBreadth(){
            return this->b;
        }

        int getheight(){
            return this->h;
        }

        long CalculateVolume(){
            return long(l) * long(b) * long(h);
        }
};


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

```
