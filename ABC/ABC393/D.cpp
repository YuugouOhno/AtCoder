#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;           // 文字列の長さ
    string S;
    cin >> S;           // 0,1からなる文字列（長さN）

    // 1. Sの中で '1' が出現するインデックスを全部集める
    vector<long long> pos;  // 1 の位置を格納するベクタ (long long にしておくのが無難)
    for (int i = 0; i < N; i++) {
        if (S[i] == '1') {
            pos.push_back(i);
        }
    }

    // 1 が全くないケースは問題文で "1が1つ以上含まれること保証" なので省略してOK

    // 2. 1 の個数 k
    long long k = (long long)pos.size();
    // 3. メディアンインデックスを計算
    //    k=5 なら mid=2 (0,1,2,3,4 の真ん中)
    //    k=4 なら mid=2 (0,1,2,3 のとき、2は中心付近のどちらかを取ればOK)
    long long mid = k / 2;

    // 4. メディアンの実インデックス
    long long medianPos = pos[mid];

    // 5. 必要操作回数(合計移動量)を求める
    //    i番目の1を "medianPos - mid + i" に動かす → 距離は abs(pos[i] - (medianPos - mid + i))
    long long ans = 0LL;
    for (long long i = 0; i < k; i++) {
        long long target = (medianPos - mid + i); // i番目の1の理想位置
        ans += llabs(pos[i] - target);
    }

    cout << ans << "\n";
    return 0;
}
