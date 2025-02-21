#include <iostream>
using namespace std;

int main () {
    string s1,s2;
    cin >> s1 >> s2;

    if (s1 == "fine" and s2 == "fine") {
        cout << "4" << endl;
    }
    if (s1 == "sick" and s2 == "sick") {
        cout << "1" << endl;
    }
    if (s1 == "sick" and s2 == "fine") {
        cout << "2" << endl;
    }
    if (s1 == "fine" and s2 == "sick") {
        cout << "3" << endl;
    }

    return 0;
}