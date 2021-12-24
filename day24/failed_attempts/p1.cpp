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

bool run(vector<long long> &num) {
    map<long long, long long> mem;
    mem[addrs["x"]] = 0;
    mem[addrs["y"]] = 0;
    mem[addrs["z"]] = 0;
    mem[addrs["z"]] = 0;
    int pos = 0;
    for (auto ins : instructions) {
        // printf("x:%lld y:%lld z:%lld w:%lld \t%s\n", 
        //         mem[addrs["x"]], mem[addrs["y"]], mem[addrs["z"]], mem[addrs["w"]], ins.ins.c_str());
        if (ins.fnc == input) {
            long long val2 = num.back();
            num.pop_back();
            input(mem[ins.val1], val2);
        } else {
            long long val2 = ins.val2 <= -1000 ? mem[ins.val2] : ins.val2;
            (*ins.fnc)(mem[ins.val1], val2);
        }
    }
    // printf("%lld\n", mem[addrs["z"]]);
    return mem[addrs["z"]] == 0;
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

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    functions['n'] = input;
    functions['d'] = add;
    functions['u'] = mult;
    functions['o'] = mod;
    functions['i'] = divide;
    functions['q'] = eql;

    addrs["x"] = -1000;
    addrs["y"] = -2000;
    addrs["z"] = -3000;
    addrs["w"] = -4000;
    
    string s;
    while (getline(cin, s)) {
        char s1t[4], s2t[4];
        if (s[1] == 'n') {
            sscanf(s.substr(s.find(' ')).c_str(), "%s", s1t);
            s2t[0] = 'x';
        }
        else {
            sscanf(s.substr(s.find(' ')).c_str(), "%s %s", s1t, s2t);
        }
        string s1 = s1t;
        string s2 = s2t;
        int val2 = is_number(s2) ? stoi(s2) : addrs[s2];
        instruction i = {
            functions[s[1]],
            addrs[s1],
            val2,
            s
        };
        instructions.push_back(i);
        // cout << s1 << s2 << s3 << endl;
    }
    // try first 4 digits for experimenting
    
    // int places = 5;
    // long long constant = pow10(14 - places);
    // for (int i = 0; i < pow10(places); ++i) {
    //    long long j = i * constant + 111111111;
    //    string num = std::to_string(j);
    //    if (num.find('0') != string::npos) continue;
    //    if (run(num)) {
    //        cout << num;
    //        break;
    //    }
    //}
    //return 0;
    
    for (long long i = 9999999999999; i > 1000000000000; --i) {
        if (!((99999999999999 - i) % 100000)) cout << i << endl;
        long long j = i;
        vector<long long> v;
        bool flag = false;
        while (j != 0) {
            long long a = j % 10;
            if (a == 0) {
                flag = true;
                break;
            }
            j /= 10;
            v.push_back(a);
        }
        if (flag) continue;
        if (run(v)) {
            cout << i << endl;
            break;
        }
    }
}
