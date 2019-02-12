cppCode = """
#include<iostream>
using namespace std;
int main(){
    return 0;
}
"""

print(cppCode)

file = open("MyProg.cpp","w")
file.write(cppCode)
file.close()

print(">> Data Written in File")