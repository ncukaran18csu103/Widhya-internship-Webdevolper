#include<iostream>
#include<cmath>
 
using namespace std;

int main()
{
    float d , x1 , x2 , y2 , y1 ;
    cin>>x1>>y1>>x2>>y2;
    d = pow((pow((x2 - x1), 2) + pow(( y2 - y1 ) , 2)) , 0.5);
    cout<<d;
    return 0;
}