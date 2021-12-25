#include <string>
#include <map>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

struct TargetInputPair {
    long long zn;
    long long I;
    int pos;
};

long long get_pair_hash(TargetInputPair pair) {
    return pair.zn * 10000 + pair.I * 100 + pair.pos;
}

typedef struct TargetInputPair TargetInputPair;

class Execution {
private:
    int k1;
    int k2;
    int k3;
    int pos;

    inline bool valid_pair(int I, long long zn, long long part2, long long target) const {
            
        long long xn = zn % 26 + k1;
        long long zn_ = zn / k3;
        int c1 = xn == I ? 1 : 26;
        int c2 = xn == I ? 0 : 1;

        long long zn_1 = c1 * zn_ + c2 * part2;
        return zn_1 == target;
    }
public:
    Execution(int k1, int k2, int k3, int pos) {
        this->k1 = k1;
        this->k2 = k2;
        this->k3 = k3;
        this->pos = pos;
    }

    vector<TargetInputPair> get_possible_inputs(long long target) const {
        long long target_og = target;
        vector<TargetInputPair> possible;
        for (int I = 1; I < 10; ++I) {
            long long part2 = I + k2;
            long long target_ = target - part2;

            for (long long zn = (target-2)*k3; zn <= (target+2)*k3; ++zn) {
                if (valid_pair(I, zn, part2, target)) possible.push_back((TargetInputPair){zn, I, pos});
            }
            for (long long zn = (target_-2)*k3; zn <= (target_+2)*k3; ++zn) {
                if (valid_pair(I, zn, part2, target)) possible.push_back((TargetInputPair){zn, I, pos});
            }
            for (long long zn = ((target-1)*k3-2)/26 - 26; zn <= ((target+1)*k3+2)/26 + 26; ++zn) {
                if (valid_pair(I, zn, part2, target)) possible.push_back((TargetInputPair){zn, I, pos});
            }
            for (long long zn = ((target_-1)*k3-2)/26 - 26; zn <= ((target_+1)*k3+2)/26 + 26; ++zn) {
                if (valid_pair(I, zn, part2, target)) possible.push_back((TargetInputPair){zn, I, pos});
            }
        }
        return possible;
    }
};

vector<Execution> executions;

map<long long, vector<string>> memo;
vector<string> solve(int position, long long target) {
    if (position == 14) {
        if (target) return vector<string>();
        vector<string> a;
        a.push_back("");
        return a;
    }

    Execution e = executions[13 - position];
    auto x = e.get_possible_inputs(target);
    vector<string> solves;
    for (auto p : x) {
        vector<string> this_solves;
        long long p_hash = get_pair_hash(p);
        if (!memo.count(p_hash)) memo.insert({p_hash, solve(position+1, p.zn)});
        this_solves = memo[p_hash];
        for (string s : this_solves) {
            solves.push_back(s + to_string(p.I));
        }
    }
    return solves;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    string s;
    int cnt = 0;

    int k1, k2, k3;
    
    while (getline(cin, s)) {
        char s1t[4], s2t[4];
        if (s[1] == 'n') {
            sscanf(s.substr(s.find(' ')+1).c_str(), "%s", s1t);
            s2t[0] = 'x';
        }
        else {
            sscanf(s.substr(s.find(' ')+1).c_str(), "%s %s", s1t, s2t);
        }
        string s1 = s1t;
        string s2 = s2t;
        if (cnt != 0 and cnt % 18 == 0) executions.push_back(Execution(k1, k2, k3, cnt / 18 - 1));
        else if (cnt % 18) {
            if (cnt % 18 == 4) k3 = stoi(s2);
            else if (cnt % 18 == 5) k1 = stoi(s2);
            else if (cnt % 18 == 15) k2 = stoi(s2);
        }

        cnt += 1;
    }
    
    executions.push_back(Execution(k1, k2, k3, cnt / 18 - 1));

    auto solves = solve(0, 0);

    sort(solves.begin(), solves.end());

    cout << "min: " << solves[0] << " max: " << solves[solves.size()-1] << endl;

    return 0;
    
}
