#include<bits/stdc++.h>
using namespace std;

int main () {
    int a, b;
    cin >> a >> b; // ２つの整数を入力

    if ((a * b) % 2 == 0) {
        cout << "Even" << endl;
    } else {
        cout << "Odd" << endl;
    }

    return 0;
}