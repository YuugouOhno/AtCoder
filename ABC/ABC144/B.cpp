#include <iostream>
using namespace std;


int main() {
    int N;
    cin >> N;
    string result = "No";
    for(int i = 1;i<=9;i++){
        for(int j = 1;j<=9;j++){
            if(i*j==N){
                result = "Yes";
                cout << result; // すぐに出力
                return 0; // 早期終了
            }
        }
    }
    cout << result;
    return 0;
}

// int main() {
//     int N;
//     cin >> N;

//     for (int i = 1; i <= 9; i++) {
//         if (N % i == 0 && N / i <= 9) {
//             cout << "Yes";
//             return 0;  // 早期終了
//         }
//     }
    
//     cout << "No";
//     return 0;
// }