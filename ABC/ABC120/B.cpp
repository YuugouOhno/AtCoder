#include <iostream>
using namespace std;

int main() {
    int A,B,K;
    cin >> A >> B >>K;
    int count = 0;
    for(int i=B;i>=1;i--){
        if(A%i == 0 and B%i == 0){
            count++;
            if(count == K){
                cout << i << endl;
                break;
            }
        }
    }
    return 0;
}