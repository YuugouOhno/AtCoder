// #include <iostream>
// using namespace std;


// int main() {
//     string S;
//     cin >> S;

//     size_t pos_circle, post_square, pos_triangle;
//     while(
//         (pos_circle=S.find("()"))!= string::npos or(post_square=S.find("[]"))!= string::npos or(pos_triangle=S.find("<>"))!= string::npos
//     ){
//         if (pos_circle!= string::npos){
//             S.replace(pos_circle,2,"");
//         }
//         if (post_square!= string::npos){
//             S.replace(post_square,2,"");
//         }
//         if (pos_triangle!= string::npos){
//             S.replace(pos_triangle,2,"");
//         }
//     }
//     cout << S;
//     return 0;
// }

#include <iostream>
#include <stack>
using namespace std;

bool isColorfulBracketSequence(const string &S) {
    stack<char> st;

    for (char c : S) {
        if (c == '(' || c == '[' || c == '<') {
            st.push(c);
        } else {
            if (st.empty()) return false; // 閉じ括弧があるのに開く括弧がない
            char top = st.top();
            if ((c == ')' && top == '(') ||
                (c == ']' && top == '[') ||
                (c == '>' && top == '<')) {
                st.pop(); // 対応するペアを削除
            } else {
                return false; // 不一致のペアが出たら不正
            }
        }
    }

    return st.empty(); // スタックが空ならOK
}

int main() {
    string S;
    cin >> S;

    if (isColorfulBracketSequence(S)) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }

    return 0;
}
