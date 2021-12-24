#include <string>
#include <map>
#include <vector>
#include <iostream>
using namespace std;

bool run(int &i1, int &i2, int &i3, int &i4, int &i5, int &i6, int &i7,
        int &i8, int &i9, int &i10, int &i11, int &i12, int &i13, int &i14) {
    long long x = 0;
    long long y = 0;
    long long z = 0;
    long long w = 0;

cout << "1:" << z << endl; w = i1;x = x * 0;x = x + z;x = x % 26;z = z / 1;x = x + 13;x = x == w;x = x == 0;y = y * 0;
y = y + 25;y = y * x;y = y + 1;z = z * y;y = y * 0;y = y + w;y = y + 13;y = y * x;z = z + y;cout << "2:" << z << endl; w = i2;
x = x * 0;x = x + z;x = x % 26;z = z / 1;x = x + 11;x = x == w;x = x == 0;y = y * 0;y = y + 25;y = y * x;
y = y + 1;z = z * y;y = y * 0;y = y + w;y = y + 10;y = y * x;z = z + y;cout << "3:" << z << endl; w = i3;x = x * 0;x = x + z;
x = x % 26;z = z / 1;x = x + 15;x = x == w;x = x == 0;y = y * 0;y = y + 25;y = y * x;y = y + 1;z = z * y;
y = y * 0;y = y + w;y = y + 5;y = y * x;z = z + y;cout << "4:" << z << endl; w = i4;x = x * 0;x = x + z;x = x % 26;z = z / 26;
x = x + -11;x = x == w;x = x == 0;y = y * 0;y = y + 25;y = y * x;y = y + 1;z = z * y;y = y * 0;y = y + w;
y = y + 14;y = y * x;z = z + y;cout << "5:" << z << endl; w = i5;x = x * 0;x = x + z;x = x % 26;z = z / 1;x = x + 14;x = x == w;
x = x == 0;y = y * 0;y = y + 25;y = y * x;y = y + 1;z = z * y;y = y * 0;y = y + w;y = y + 5;y = y * x;
z = z + y;cout << "6:" << z << endl; w = i6;x = x * 0;x = x + z;x = x % 26;z = z / 26;x = x + 0;x = x == w;x = x == 0;y = y * 0;
y = y + 25;y = y * x;y = y + 1;z = z * y;y = y * 0;y = y + w;y = y + 15;y = y * x;z = z + y;cout << "7:" << z << endl; w = i7;
x = x * 0;x = x + z;x = x % 26;z = z / 1;x = x + 12;x = x == w;x = x == 0;y = y * 0;y = y + 25;y = y * x;
y = y + 1;z = z * y;y = y * 0;y = y + w;y = y + 4;y = y * x;z = z + y;cout << "8:" << z << endl; w = i8;x = x * 0;x = x + z;
x = x % 26;z = z / 1;x = x + 12;x = x == w;x = x == 0;y = y * 0;y = y + 25;y = y * x;y = y + 1;z = z * y;
y = y * 0;y = y + w;y = y + 11;y = y * x;z = z + y;cout << "9:" << z << endl; w = i9;x = x * 0;x = x + z;x = x % 26;z = z / 1;
x = x + 14;x = x == w;x = x == 0;y = y * 0;y = y + 25;y = y * x;y = y + 1;z = z * y;y = y * 0;y = y + w;
y = y + 1;y = y * x;z = z + y;cout << "10:" << z << endl; w = i10;x = x * 0;x = x + z;x = x % 26;z = z / 26;x = x + -6;x = x == w;
x = x == 0;y = y * 0;y = y + 25;y = y * x;y = y + 1;z = z * y;y = y * 0;y = y + w;y = y + 15;y = y * x;
z = z + y;cout << "11:" << z << endl; w = i11;x = x * 0;x = x + z;x = x % 26;z = z / 26;x = x + -10;x = x == w;x = x == 0;y = y * 0;
y = y + 25;y = y * x;y = y + 1;z = z * y;y = y * 0;y = y + w;y = y + 12;y = y * x;z = z + y;cout << "12:" << z << endl; w = i12;
x = x * 0;x = x + z;x = x % 26;z = z / 26;x = x + -12;x = x == w;x = x == 0;y = y * 0;y = y + 25;y = y * x;
y = y + 1;z = z * y;y = y * 0;y = y + w;y = y + 8;y = y * x;z = z + y;cout << "13:" << z << endl; w = i13;x = x * 0;x = x + z;
x = x % 26;z = z / 26;x = x + -3;x = x == w;x = x == 0;y = y * 0;y = y + 25;y = y * x;y = y + 1;z = z * y;
y = y * 0;y = y + w;y = y + 14;y = y * x;z = z + y;cout << "14:" << z << endl; w = i14;x = x * 0;x = x + z;x = x % 26;z = z / 26;
x = x + -5;x = x == w;x = x == 0;y = y * 0;y = y + 25;y = y * x;y = y + 1;z = z * y;y = y * 0;y = y + w;
y = y + 9;y = y * x;z = z + y;

    cout << "val: " << z << endl;
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

    int i1 = 9, i2 = 9, i3 = 9, i4 = 9, i5 = 9, i6 = 9, i7 = 9, i8 = 9, i9 = 9,
        i10 = 9, i11 = 9, i12 = 9, i13 = 9, i14 = 9;
    int *locations[] = {&i1, &i2, &i3, &i4, &i5, &i6, &i7, &i8, &i9, &i10,
        &i11, &i12, &i13, &i14};
    while (1) {
        int loc, val;
        cout << "12345678901234" << endl;
        cout << i1 << i2 << i3 << i4 << i5 << i6 << i7 << i8 << i9 << i10
            << i11 << i12 << i13 << i14 << endl;
        cin >> loc >> val;
        if (loc > 14) continue;
        *locations[loc-1] = val;

        if (run(i1, i2, i3, i4, i5, i6, i7, i8,
                    i9, i10, i11, i12, i13, i14) == 0) {
            cnt += 1;
        cout << i1 << i2 << i3 << i4 << i5 << i6 << i7 << i8 << i9 << i10
            << i11 << i12 << i13 << i14 << endl;
        return 0;
        }
    }
}
