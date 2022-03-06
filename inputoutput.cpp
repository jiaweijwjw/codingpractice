#include <bits/stdc++.h>
using namespace std;

#define MAX_LEN 100
#define delim ','

static inline void trimLeft(string &str) {
    // erase first, last, not inclusive of last.
    str.erase(str.begin(), find_if(str.begin(), str.end(), [](unsigned char ch) { return !isspace(ch); }));
}
static inline void trimRight(string &str) {
    str.erase(find_if(str.rbegin(), str.rend(), [](unsigned char ch){ return !isspace(ch); }).base(), str.end());
    // we have to use .base() because the erase(first, last) is inclusive. if we remove the find_if rit, it will remove the last char also (which is the first char found)
}
static inline void trimBothEnds(string &str) {
    trimLeft(str);
    trimRight(str);
}
class trimmer {
    public:
    void operator()(string &str1, string &str2) {
        trimBothEnds(str1);
        trimBothEnds(str2);
    }
    void operator()(string &str) {
        trimBothEnds(str);
    }
};

int main() {
    // // dont use this since this works with C char arrays
    // cout << "Enter your name: ";
    // char buf[MAX_LEN];
    // cin.getline(buf, MAX_LEN);
    // cout << buf << endl;

    // // use this instead, works with C++ strings.
    // string temp;
    // cout << "more details about you: ";
    // getline(cin, temp);
    // cout << temp << endl;
    
    // if we dont know how many line of input can use vector since variable size.
    string nameAndAge;
    vector<tuple<int, int>> vect;
    while (getline(cin, nameAndAge)) { // getline() not cin.getline()
        istringstream iss(nameAndAge);
        string str1, str2;
        getline(iss, str1, delim);
        getline(iss, str2);
        trimmer trimmer;
        trimmer(str1, str2);
        // or:
        // trimmer(str1);
        // trimmer(str2);
        int val1 = stoi(str1);
        int val2 = stoi(str2);
        tuple<int, int> pair;
        pair = make_tuple(val1, val2);
        vect.emplace_back(pair);
    }
    cout << vect.size() << endl;
    // ranged based for loop
    for (auto tup : vect) {
        cout << get<0>(tup) << " " << get<1>(tup) << endl;
    }
    return 0;
}