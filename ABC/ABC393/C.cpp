#include <iostream>   // cin, cout を使うのに必要
#include <map>        // pair をキーにした map を使うのに必要
#include <utility>    // pair を使うのに必要
#include <algorithm>  // min, max を使うのに必要
using namespace std;

int main() {
    ios::sync_with_stdio(false); // 入出力を高速化するおまじない（なくてもOK）
    cin.tie(nullptr);            // 同上

    // 頂点数 N, 辺数 M
    int N, M;
    cin >> N >> M;

    long long removeCount = 0; // 削除する辺の数を数える変数

    // pair<int,int> をキーにして、その「出現回数」をカウントする map
    // 例: map[ {1,2} ] = 3 なら、「(1,2) の辺が合計で 3 回出た」ってこと
    map< pair<int,int>, long long > edgeCount;

    for (int i = 0; i < M; i++) {
        int u, v;
        cin >> u >> v;

        // 1. 「頂点が同じ」つまり自己ループ(ループ辺)なら無条件で削除
        if (u == v) {
            removeCount++;
        } else {
            // 2. 無向グラフなので (u,v) と (v,u) は同じ「辺のペア」と扱う
            //    つまり (小さい方, 大きい方) で統一して管理するといい
            int a = min(u, v);
            int b = max(u, v);
            edgeCount[{a, b}]++;
        }
    }

    // 3. 多重辺の処理
    //    同じ (a,b) のペアが複数あったら、1本以外は削除する必要がある
    //    例: 出現回数 c 本あれば、残せるのは 1 本だけなので c-1 は削除！
    for (auto &kv : edgeCount) {
        long long c = kv.second; // そのペア (a,b) の出現回数
        // 「c 本のうち 1 本だけ残し、他は削除」だから (c - 1) を削除数に足す
        removeCount += (c - 1);
    }

    // 4. 結果の出力
    cout << removeCount << "\n";

    return 0;
}
