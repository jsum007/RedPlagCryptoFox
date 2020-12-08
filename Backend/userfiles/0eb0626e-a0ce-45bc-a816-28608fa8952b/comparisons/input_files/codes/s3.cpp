#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <tuple>
#include <numeric>
#include <iomanip>
#include <deque>
#include <set>
#include <cmath>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <ext/pb_ds/assoc_container.hpp>
#include <functional>
using namespace std;
using namespace __gnu_pbds;
typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> ordered_set;
int query(int i, int j, vector<vector<int>> & st, vector<int> & log) {
    int k = log[j - i + 1];
    return min(st[k][i], st[k][j - (1 << k) + 1]);
}
void solve() {
    int n;
    cin >> n;
    vector<int> a(n + 1), cnt(n + 1), log(n + 1);
    if (n == 1) {
        cout << 1 << endl;
        return;
    }
    for (int i = 1; i <= n; ++i)
        cin >> a[i];
    for (int i = 1; i <= n; ++i)
        ++cnt[a[i]];
    cout << (*max_element(cnt.begin(), cnt.end()) == 1);
    for (int i = 2; i <= n; ++i)
        log[i] = log[i / 2] + 1;
    vector<vector<int>> st(log[n] + 1);
    st[0] = a;
    for (int i = 1; i <= log[n]; ++i) {
        st[i].resize(n - (1 << i) + 2);
        for (int j = 1; j + (1 << i) - 1 <= n; ++j)
            st[i][j] = min(st[i - 1][j], st[i - 1][j + (1 << (i - 1))]);
    }
    int l = 1, r = n;
    while (l + 1 < r) {
        int md = (l + r) / 2;
        vector<int> t(n - md + 2), count(n + 1);
        for (int i = 1; i <= n - md + 1; ++i)
            t[i] = query(i, i + md - 1, st, log);
        for (int i = 1; i < t.size(); ++i)
            ++count[t[i]];
        if (*max_element(count.begin(), count.end()) == 1 && *max_element(t.begin(), t.end()) < t.size())
            r = md;
        else
            l = md;
    }
    cout << string(r - 2, '0') << string(n - r, '1') << bool(cnt[1]) << endl;
}
int main() {
    int t;
    cin >> t;
    while (t--)
        solve();
    return 0;
}