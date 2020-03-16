#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;
const int MAXN = 1000000;

double Rand(double L, double R)
{
    /* Param1: Left border
       Param2: Right border
       return: A random double number between L and R
    */
    return L + (R - L) * rand() * 1.0 / RAND_MAX;
}
double get_pi()
{
    srand(time(NULL));
    int cnt = 0;
    for(int i = 0; i < MAXN; ++i)
    {
        double x = Rand(-1, 1);
        double y = Rand(-1, 1);
        if(x * x + y * y <= 1)
            cnt ++;
    }
    return cnt * 4.0 / MAXN ;
}
int main()
{
    int i;
    double ans = 0;
    for(i = 0; i < 10; ++i)
        ans += get_pi();
    ans /= 10;
    cout << "Congratulations, We can figure out PI approximately : " << ans << endl;
    return 0;
}
