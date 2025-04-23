#include <iostream>
using namespace std;

int main() {
    int N;
    string S;
    int error_count= 0;
    bool is_login = false;
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> S;
        if (S == "login") {
            is_login = true;
        } else if (S == "logout") {
            is_login = false;
        }
        if (!is_login && S == "private") {
            error_count++;
        }
    }
    cout << error_count << endl;
    return 0;
}