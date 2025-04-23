#include <iostream>
using namespace std;

unsigned getDigit(unsigned n) {
    unsigned digit = 0;
    while(n != 0){
        n /= 10;
        digit++;
    }
    return digit;
}

int main() {
    int N;
    cin >> N;

    int count = 0;
    for (int i = 1; i <= N; ++i){
        unsigned digit;
        digit = getDigit(i);
        if (digit & 1){
            count++;
        }
    }
    cout << count;
    return 0;
}