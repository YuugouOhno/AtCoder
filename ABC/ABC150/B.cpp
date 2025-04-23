#include <iostream>
using namespace std;

int main(){
    int N;
    string S;
    cin >> N;
    cin >> S;

    int result = 0;
    for(int i=0;i<N-2;i++){
        if(S[i]=='A' and S[i+1]=='B' and S[i+2]=='C'){
            result++;
        }
    }
    cout << result;
}