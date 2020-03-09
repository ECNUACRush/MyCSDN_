#include <iostream>
#include <algorithm>
#include <cstdio>
#define MAXN 10009
using namespace std;
typedef long long ll;

struct my_sort
{
    ll num;  // 输入的数
    int cnt;  // '1'的个数
};
bool cmp(my_sort p1, my_sort p2)//  sort 
{
    return (p1.cnt == p2.cnt) ? p1.num < p2.num : p1.cnt > p2.cnt;
}
int q_cmp(const void* a, const void* b)//  qsort
{
    struct my_sort d1,d2;
    d1=*((struct my_sort *)a);
    d2=*((struct my_sort *)b);
    if(d2.cnt!=d1.cnt)  
         return d2.cnt-d1.cnt;
    else
    {    
        if(d1.num>d2.num) return 1;
        else return -1;
    }
}
int main()
{
    int T, i, j, N;
    cin >> T;
    for(i = 0; i < T; ++i)
    {
        my_sort S[MAXN];
        cin >> N;
        for(j = 0; j < N; ++j)
        {
            cin >> S[j].num;
            S[j].cnt = 0;
            ll and_num = 1, k = 0;
            while(k < 64)   //  Core code
            {
            // 通过初始用1，每次左移1位与我们需要判断的数据作‘&’操作，来判断有多少个‘1’。
                if(S[j].num & and_num) S[j].cnt++;
                and_num = and_num << 1;
                k++;
            }
        }
        //sort(S, S+N, cmp);
        qsort(S, N, sizeof(S[0]), q_cmp);
        printf("case #%d:\n", i);
        for(j = 0; j < N; ++j)
            cout << S[j].num << ((j == N - 1) ? '\n' : ' ');
    }
    return 0;
}

