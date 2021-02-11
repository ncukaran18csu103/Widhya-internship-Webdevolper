#include<iostream>
#include<cmath>
#include<vector>
#include<algorithm>
 
using namespace std;

int distance_sum(vector<int> arr ,int n)
{
    sort(arr.begin() , arr.end());
    int res = 0 , sum = 0;
    for(int i = 0 ; i < n ; i++)
    {
        res += (arr[i] * i - sum);
        sum += arr[i];
    }
    return res;
}

int totaldistancesum(vector<int> x , vector<int> y , int n)
{
    return (distance_sum(x , n) + distance_sum(y , n));
}

int main()
{
    int n;
    cin>>n;
    vector<int> x , y;
    for(int i = 0 ; i < n ; i++)
    {
        int k;
        cin>>k;
        x.push_back(k);
    }
    for(int i = 0 ; i < n ; i++)
    {
        int k;
        cin>>k;
        y.push_back(k);
    }    
    int result = totaldistancesum(x , y , n);
    cout<<result;
    return 0;
}