#include<string>
#include<iostream>
#include<sstream>
#include<algorithm>
#include<vector>
#include<cstdio>
using namespace std;

string alphaet;

bool cmp(string aa,string bb)
{
  int len1 = aa.size(), len2 = bb.size();
  for(int i = 0; i < min(len1, len2); ++i)
  {
    char c1 = toupper(aa[i]), c2 = toupper(bb[i]);
    if(c1 != c2)
     return alphaet.find(c1,0) < alphaet.find(c2,0);
  }
  return len1 < len2;
}

int main()
{
  string line,t;
  vector <string> s;
  while(cin >> alphaet)
  {
     char ch;
     s.clear();
     while(1)
     {
         cin >> t;
         ch = getchar();
         s.push_back(t);
         if(ch == '\n') break;
     }
  	 sort(s.begin(), s.end(), cmp);
  	 int len = s.size();
  	 for(int i = 0; i < len; ++i)
        cout << s.at(i) << ((i == len - 1)?'\n':' ');
  }
  return 0;
}


