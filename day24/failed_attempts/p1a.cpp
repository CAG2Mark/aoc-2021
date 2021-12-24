#include <string>
#include <map>
#include <vector>
#include <iostream>
using namespace std;

void add(long long &a, long long b) {
    // printf("add %lld + %lld\n", a, b);
    a += b;
}
void mult(long long &a, long long b) {
    a *= b;
}
void mod(long long &a, long long  b) {
    a %= b;
    if (a < 0) a += b;
}
void divide(long long &a, long long b) {
    a /= b;
}
void eql(long long &a, long long b) {
    a = a == b;
}

void input(long long &a, long long b) {
    a = b;
}

typedef void (*alu_function)(long long &, long long); 
map<char, alu_function> functions;
map<string, long long> addrs;
struct instruction {
    alu_function fnc;
    long long val1;
    long long val2;
    string ins;
};
typedef struct instruction instruction;
vector<instruction> instructions;

bool run(int &i1, int &i2, int &i3, int &i4, int &i5, int &i6, int &i7,
        int &i8, int &i9, int &i10, int &i11, int &i12, int &i13, int &i14) {
    int pos = -1;
    long long x;
    long long y;
    long long z;
    long long w;
w = i1;x = x * 0;x = x + z;x = x % 26;z = z / 1;x = x + 13;x = x == w;x = x == 0;y = y * 0;
y = y + 25;y = y * x;y = y + 1;z = z * y;y = y * 0;y = y + w;y = y + 13;y = y * x;z = z + y;w = i2;
x = x * 0;x = x + z;x = x % 26;z = z / 1;x = x + 11;x = x == w;x = x == 0;y = y * 0;y = y + 25;y = y * x;
y = y + 1;z = z * y;y = y * 0;y = y + w;y = y + 10;y = y * x;z = z + y;w = i3;x = x * 0;x = x + z;
x = x % 26;z = z / 1;x = x + 15;x = x == w;x = x == 0;y = y * 0;y = y + 25;y = y * x;y = y + 1;z = z * y;
y = y * 0;y = y + w;y = y + 5;y = y * x;z = z + y;w = i4;x = x * 0;x = x + z;x = x % 26;z = z / 26;
x = x + -11;x = x == w;x = x == 0;y = y * 0;y = y + 25;y = y * x;y = y + 1;z = z * y;y = y * 0;y = y + w;
y = y + 14;y = y * x;z = z + y;w = i5;x = x * 0;x = x + z;x = x % 26;z = z / 1;x = x + 14;x = x == w;
x = x == 0;y = y * 0;y = y + 25;y = y * x;y = y + 1;z = z * y;y = y * 0;y = y + w;y = y + 5;y = y * x;
z = z + y;w = i6;x = x * 0;x = x + z;x = x % 26;z = z / 26;x = x + 0;x = x == w;x = x == 0;y = y * 0;
y = y + 25;y = y * x;y = y + 1;z = z * y;y = y * 0;y = y + w;y = y + 15;y = y * x;z = z + y;w = i7;
x = x * 0;x = x + z;x = x % 26;z = z / 1;x = x + 12;x = x == w;x = x == 0;y = y * 0;y = y + 25;y = y * x;
y = y + 1;z = z * y;y = y * 0;y = y + w;y = y + 4;y = y * x;z = z + y;w = i8;x = x * 0;x = x + z;
x = x % 26;z = z / 1;x = x + 12;x = x == w;x = x == 0;y = y * 0;y = y + 25;y = y * x;y = y + 1;z = z * y;
y = y * 0;y = y + w;y = y + 11;y = y * x;z = z + y;w = i9;x = x * 0;x = x + z;x = x % 26;z = z / 1;
x = x + 14;x = x == w;x = x == 0;y = y * 0;y = y + 25;y = y * x;y = y + 1;z = z * y;y = y * 0;y = y + w;
y = y + 1;y = y * x;z = z + y;w = i10;x = x * 0;x = x + z;x = x % 26;z = z / 26;x = x + -6;x = x == w;
x = x == 0;y = y * 0;y = y + 25;y = y * x;y = y + 1;z = z * y;y = y * 0;y = y + w;y = y + 15;y = y * x;
z = z + y;w = i11;x = x * 0;x = x + z;x = x % 26;z = z / 26;x = x + -10;x = x == w;x = x == 0;y = y * 0;
y = y + 25;y = y * x;y = y + 1;z = z * y;y = y * 0;y = y + w;y = y + 12;y = y * x;z = z + y;w = i12;
x = x * 0;x = x + z;x = x % 26;z = z / 26;x = x + -12;x = x == w;x = x == 0;y = y * 0;y = y + 25;y = y * x;
y = y + 1;z = z * y;y = y * 0;y = y + w;y = y + 8;y = y * x;z = z + y;w = i13;x = x * 0;x = x + z;
x = x % 26;z = z / 26;x = x + -3;x = x == w;x = x == 0;y = y * 0;y = y + 25;y = y * x;y = y + 1;z = z * y;
y = y * 0;y = y + w;y = y + 14;y = y * x;z = z + y;w = i14;x = x * 0;x = x + z;x = x % 26;z = z / 26;
x = x + -5;x = x == w;x = x == 0;y = y * 0;y = y + 25;y = y * x;y = y + 1;z = z * y;y = y * 0;y = y + w;
y = y + 9;y = y * x;z = z + y;
    return z;
} 

bool is_number(const string& str){
    for (char const &c : str) {
        if (std::isdigit(c) == 0 and c != '-') return false;
    }
    return true;
}

inline long long pow10(int n) {
    long long x = 1;
    for (int i = 0; i < n; ++i) {
        x *= 10;
    }
    return x;
}

long long cnt = 0;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    for (int i1 = 5; i1 > 0; --i1)
    for (int i2 = 9; i2 > 0; --i2)
    for (int i3 = 9; i3 > 0; --i3)
    for (int i4 = 9; i4 > 0; --i4)
    for (int i5 = 9; i5 > 0; --i5)
    for (int i6 = 9; i6 > 0; --i6)
    for (int i7 = 9; i7 > 0; --i7)
    for (int i8 = 9; i8 > 0; --i8)
    for (int i9 = 9; i9 > 0; --i9)
    for (int i10 = 9; i10 > 8; --i10)
    for (int i11 = 9; i11 > 8; --i11)
    for (int i12 = 9; i12 > 8; --i12)
    for (int i13 = 9; i13 > 0; --i13)
    for (int i14 = 9; i14 > 0; --i14) {
        cnt += 1;
            if (cnt % 100000000 == 0) {
        cout << i1 << i2 << i3 << i4 << i5 << i6 << i7 << i8 << i9 << i10
            << i11 << i12 << i13 << i14 << endl;
            }
        if (run(i1, i2, i3, i4, i5, i6, i7, i8,
                    i9, i10, i11, i12, i13, i14) == 0) {
            cnt += 1;
        cout << "found " << i1 << i2 << i3 << i4 << i5 << i6 << i7 << i8 << i9 << i10
            << i11 << i12 << i13 << i14 << endl;
        return 0;
        }
    }
}
