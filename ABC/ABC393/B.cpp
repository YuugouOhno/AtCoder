#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main () {
    string S;
    vector<int> A_list,B_list,C_list;
    cin >> S;

    for (int i=0; i < S.size(); i++) {
        if (S[i] == 'A') A_list.push_back(i);
        else if (S[i] == 'B') B_list.push_back(i);
        else if (S[i] == 'C') C_list.push_back(i);
    }

    int count = 0;

    // A を固定
    for (int i : A_list) {
        // B の位置を二分探索で探す
        auto b_start = upper_bound(B_list.begin(), B_list.end(), i);
        for (auto it = b_start; it != B_list.end(); ++it) {
            int j = *it;
            int d = j - i;  // A から B までの距離
            int k = j + d;  // C の期待される位置
            
            // C の位置を二分探索で探す
            if (binary_search(C_list.begin(), C_list.end(), k)) {
                count++;
            }
        }
    }
    cout << count;
    return 0;
}