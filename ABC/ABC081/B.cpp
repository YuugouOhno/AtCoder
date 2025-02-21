#include<bits/stdc++.h>
using namespace std;

int N;
int A[222];

int main() {
    cin >> N;
    for (int i=0; i<N; ++i) cin >> A[i];

    int res = 0;

    while (true) {
        bool is_break = false;
        for (int i=0; i < N; ++i) {
            if (A[i]%2==0){
                A[i] = A[i]/2;
            } else {
                is_break = true;
            }
        }
        if (is_break) break;
        res = ++res;
    }

    cout << res << endl;


}