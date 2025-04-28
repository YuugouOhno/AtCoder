#include <iostream>
using namespace std;

int main() {
    int N;
    string result;
    cin >> N;
    if(N%2==0){
        result += "==";
        for(int i=0;i<N/2-1;i++){
        result = "-" + result + "-";
    }
    } else {
        result += "=";
        for(int i=0;i<N/2;i++){
        result = "-" + result + "-";
    }
    }
    
    cout << result << endl;
}