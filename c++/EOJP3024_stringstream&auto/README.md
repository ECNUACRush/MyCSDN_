# 					StringStream使用强化

### 核心代码：

```cpp
void solve()/* Define function solve() to process one case of the problem    */
{
    string s, t;
    set<string> ss;
    getline(cin, s);
    for(auto &i : s)
        if(!isalpha(i)) i = ' ';
    stringstream stream(s);
    while(stream >> t)
        ss.insert(t);
    auto x = ss.begin();
    cout << *x;
    while(++x != ss.end())
        cout << ' ' << *x;
    cout << endl;
    return ;
}
```

