#include <iostream>
#include <cmath>
using namespace std;

int digit_length(long long x) {
    return (x == 0) ? 1 : (int)log10(x) + 1;
}

int main() {
    long long N;
    cin >> N;
    int result = 1000000;

    for(long long i=1;i*i<=N;i++){
        if(N%i==0){
            long long A = i, B = N / i;
            result = min(result, max(digit_length(A), digit_length(B)));
        }
    }

    cout << result << endl;
    return 0;
}
