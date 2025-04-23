#include <iostream>
using namespace std;


int main() {
    string S;
    cin >> S;
    int W_count = 0;
    for (int i=0; i < S.size();i++) {
        if (S[i] == 'W') {
            W_count++;
        } else if (W_count and S[i] == 'A') {
            S[i-W_count] = 'A';
            for (int j = 0;j<W_count;j++){
                S[i-j] = 'C';
            }
            W_count = 0;
        } else {
            W_count = 0;
        }
    }
    cout << S;
    return 0;
}