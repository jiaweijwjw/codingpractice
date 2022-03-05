#include <iostream>
#include <string>
#include <vector>
#include <bits/stdc++.h> // to include every library, not recommended to use this in real SE projects
using namespace std;

int main() {

    ios::sync_with_stdio(false); cin.tie(NULL); // to make cin/cout faster
    
    // printing
    cout << "some string" << endl; // endl is for newline
    // reading
    string name;
    cin >> name;

    // variables use camelCase. c++ is statically typed. Statically typed is a programming language characteristic in which variable types are explicitly declared 
    // can have unsigned
    // c doesnt have strings but c++ have
    // float need to add f behind, but usually just use double
    // const cant be modified, and use UPPERCASE
    // casting: (int)3.56, from double to int
    string someString = "helloworld";
    char someChar = 'A';
    // google c++ string functions

    // pointers
    // & is the address
    // pointers must be the same type as the variable it is pointing to
    int num = 10;
    int *iptr = &num;
    // if u print iptr, it will be the mem address of num which the iptr is pointing to
    // if you print *iptr, it will be dereferencing the ptr which gives the value at that address.
    // * is use to both: create and pointer AND to dereference a pointer.

    // arrays
    int someArray[] = {1,3,5};
    int emptyArrayWithSixElements[6];
    int numberGrid[2][3] = {{1,2,3}, {4,5,6}};

    // vectors are dynamic arrays, #include <vector>
    vector<string> friends; // type of string, no need declare the size 
    // google vector functions

    // functions
    // functions must be above the main function, if put below, must declare the function on top first.

    // loops
    // do while is the same as while but it checks the condition after, so the loops runs minimally once.

    // exception catching
    // try catch block
    // try {
    // // Block of code to try
    // throw exception; // Throw an exception when a problem arise
    // }
    // catch (exception type / ... for any exception type) {
    // // Block of code to handle errors
    // }

    // use classes!
    // can define our own constructors
    // private section: only code in the specified class can modify these variables, use getters and setters
    // inheritance
    // can use parents functions, define own functions or override parents functions
    // can also use the superclass constructor
    // abstract functions in superclass, meaning child class MUST override it.

    return 0;
}