#include <bits/stdc++.h>
using namespace std;

#define delim ','

static inline void trimLeft(string &str) {
    str.erase(str.begin(), find_if(str.begin(), str.end(), [](unsigned char ch){ return !isspace(ch); }));
}
static inline void trimRight(string &str) {
    str.erase(find_if(str.rbegin(), str.rend(), [](unsigned char ch){ return !isspace(ch); }).base(), str.end());
}
static inline void trimBothEnds(string &str) {
    trimLeft(str);
    trimRight(str);
}
// trying out functors
class Trimmer {
    public:
    void operator()(string &str1, string &str2) {
        trimBothEnds(str1);
        trimBothEnds(str2);
    }
};

struct Vertex {
    int item;
    Vertex* next;
};

class SLL {
    private:
    int size=0;
    Vertex* head;
    Vertex* get(int i) {
        Vertex* ptr = head;
        for (int k=0; k<i; k++) {
            ptr = ptr->next;
        }
        return ptr;
    }
    public:
    SLL(vector<int> &vect) {
        head = NULL;
        size = vect.size();
        for (int i=0; i<size; i++) {
            insertAtHead(vect.at(i));
        }
    };
    void insertAtHead(int v) {
        Vertex* new_v = new Vertex();
        new_v->item = v;
        new_v->next = head;
        head = new_v;
    };
    int getSize() {
        return size;
    };
    Vertex* getVertex(int pos) {
        return get(pos);
    };
    void printSLL() {
        Vertex* ptr = head;
        for (int i=0; i<size; i++) {
            cout << ptr->item;
            if (i != size-1 ) {
                cout << " -> ";
            }
            ptr = ptr->next;
        }
    }
};

int main() {
    // use input: N, N num of integers of original array, i, to insert, r to remove
    // N
    // array of numbers
    // num to insert, position
    ios::sync_with_stdio(false); cin.tie(NULL);
    int N;
    cin >> N;
    int num;
    vector<int> vect;
    while (N > 0) {
        cin >> num;
        vect.emplace_back(num);
        N--;
    }
    vector<tuple<int, int>> insertVect;
    string stringOfInsertionPairs;
    Trimmer trimmer;
    while(getline(cin, stringOfInsertionPairs)) {
        istringstream iss(stringOfInsertionPairs);
        string insertValStr, insertPosStr;
        getline(iss, insertValStr, delim);
        getline(iss, insertPosStr);
        trimmer(insertValStr, insertPosStr);
        int insertVal = stoi(insertValStr);
        int insertPos = stoi(insertPosStr);
        tuple<int, int> valPosPair;
        valPosPair = make_tuple(insertVal, insertPos);
        insertVect.emplace_back(valPosPair);
    }
    cout << vect.size() << endl;
    SLL slinkedlist(vect);
    slinkedlist.printSLL();
    cout << endl;
    cout << slinkedlist.getSize() << endl;
    cout << "Reverse SLL: " << endl;
    for (int i=0; i<slinkedlist.getSize(); i++) {
        cout << slinkedlist.getVertex(i)->item;
        if (i != slinkedlist.getSize()-1) {
            cout << " -> ";
        } else {
            cout << endl;
        }
    }
    for (auto tup : insertVect) {
        int val = get<0>(tup);
        int pos = get<1>(tup);
        slinkedlist.insertAtHead(val);
    }
    slinkedlist.printSLL();
    return 0;
}