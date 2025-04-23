#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int N;
    cin >> N;

    vector<string> S(N);
    for (int i = 0; i < N; i++) {
        cin >> S[i];
    }

    // 文字列を長さ順にソート
    sort(S.begin(), S.end(), [](const string &a, const string &b) {
        return a.size() < b.size();
    });

    // 連結結果を求める
    string result;
    for (const string &str : S) {
        result += str;
    }

    // 出力
    cout << result << endl;

    return 0;
}
