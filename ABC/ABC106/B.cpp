#include <iostream>
using namespace std;

int countDivisors(int n){
    int count = 0;
    for(int i=1;i*i <= n; i++){
        if(n%i == 0) {
            count++;
            if (i != n/i) count ++;
        }
    }
    return count;
}

int main(){
    int N;
    cin >> N;

    int result = 0;
    for (int i=1;i<=N;i+=2){
        if(countDivisors(i)==8){
            result++;
        }
    }
    cout<<result;
    return 0;
}
