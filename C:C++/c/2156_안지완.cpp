#include <iostream>

using namespace std;

int arr[10000];
int dp[10000];
int max(int a, int b){
    return a > b ? a : b;
}
int sol(int num){
    int maxD = 0;
    if(num == 0){ return 0;}
    if(num == 1){ return arr[0];}
    maxD = max(arr[num-1] + dp[num-3], dp[num-2]);
    return maxD;
}
int main(void){
    int N, ans = 0;
    cin >> N;
    for(int i =0 ; i < N ; i++){
        cin >> arr[i];
    }
    for(int i =0 ; i < N ;i++){
        dp[i] = sol(i) + arr[i];
        if(i>0){
            dp[i] = max(dp[i], dp[i-1]); 
        }
        ans = dp[i];
    }
    cout << ans;
}
