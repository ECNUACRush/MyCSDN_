#include <iostream>
#include <string>
#include <set>
#include <sstream> // Be remind of this head file.Plz
using namespace std;
void init()/* Define function init() to do global initialization if needed   */
{
    return ;
}
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
/******************************************************************************/
/*  DON'T MODIFY main() function anyway!                                      */
/******************************************************************************/
int main()
{
    int T, i;
    (cin >> T).get();
    for(i = 0; i < T; ++i){cout << "case #" << i << ":\n"; solve();}
    return 0;
}

