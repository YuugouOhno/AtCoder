#include <iostream>
using namespace std;


int main() {
    string S;
    cin >> S;

    string result;
    for (char c:S){
        if (c=='2'){
            result += c;
        }
    }
    cout << result;
    return 0;
}