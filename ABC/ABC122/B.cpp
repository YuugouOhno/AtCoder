#include <iostream>
using namespace std;

int main(){
    string S;
    cin >> S;
    bool isContinue = false;
    int current_len=0, max_len=0;
    for(char c : S){
        if (c == 'A' or c== 'C' or c == 'G' or c == 'T'){
            current_len ++;
            max_len=max(max_len,current_len);
        } else {
            current_len = 0;
        }
        
    }
    cout << max_len;
    return 0;
}