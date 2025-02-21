#include <iostream>
using namespace std;


int sumOfEachDigit (int N) {
    int res = 0;
    while (N>0) {
        res += N % 10;
        N /= 10; 
    }
    return res;
}

int main() {
    int N,A,B;
    cin >> N >> A >> B;

    int res = 0;
    for (int i=1;i<=N;++i){
        int sum = sumOfEachDigit(i);
        if (A <= sum && sum  <= B) {
            res += i;
        }
    }

    cout << res << endl;
}